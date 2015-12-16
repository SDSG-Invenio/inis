from datetime import date, datetime, timedelta

from flask import Blueprint, current_app, render_template
from flask.ext.breadcrumbs import register_breadcrumb
from flask.ext.login import current_user, login_required
from flask.ext.menu import current_menu, register_menu

from inis.config import CFG_MEMBERS_DICT

from invenio.base.decorators import wash_arguments
from invenio.base.i18n import _


blueprint = Blueprint(
    "inis",
    __name__,
    url_prefix="",
    template_folder="templates",  # where your custom templates will go
    static_folder="static"        # where the assets go
)


@blueprint.before_app_first_request
def register_menu_items():
    """Setup menu for INIS Input Management."""
    item = current_menu.submenu('breadcrumbs.inis')
    item.register('', '')

    item = current_menu.submenu("settings.groups")
    item.register(
        'settings.groups', _('INIS Members'), order=1,
        visible_when=lambda: current_user.is_admin
        )
    # item = current_menu.submenu('main')
    # item.register(
    #     'deposit.create', _('Input'), order=2,
    #     endpoint_arguments_constructor=lambda: dict(name='input')
    # )

    def menu_fixup():
        item = current_menu.submenu("main.webdeposit")
        item._text = "Submit"
        item = current_menu.submenu("breadcrumbs.webdeposit")
        item._text = "Submit"

        # Remove items
        item = current_menu.submenu("main")
        item._child_entries.pop('deposit', None)
        item._child_entries.pop('search', None)
        item._child_entries.pop('documentation', None)

        item = current_menu.submenu("settings.workflows")
        item.hide()
        item = current_menu.submenu("settings.applications")
        item.hide()
        item = current_menu.submenu("settings.oauthclient")
        item.hide()

        # item = current_menu.submenu("settings.groups")
        # item._text = "INIS Members"

        # Append function to end of before first request functions, to ensure
        # all menu items have been loaded.
    current_app.before_first_request_funcs.append(menu_fixup)


@blueprint.route('/help', methods=['GET', ])
@register_menu(blueprint, 'main.help', _('Help'), order=4)
@register_breadcrumb(blueprint, 'breadcrumbs.help', _("Help"))
def help():
    return render_template('inis/help.html')


@blueprint.route('/bibsched', methods=['GET', ])
@login_required
@register_menu(blueprint, 'main.bibsched', _('Bibsched'), order=5,
               visible_when=lambda: current_user.is_admin)
@register_breadcrumb(blueprint, 'breadcrumbs.bibsched', _("Queue status"))
def bibsched():

    from invenio.legacy.bibsched.cli import server_pid
    from invenio.legacy.bibsched.webapi import get_bibsched_mode, get_bibsched_tasks

    running = bool(server_pid())

    tasks = get_bibsched_tasks()
    bibsched_error = False
    for task in tasks:
        tskid, proc, priority, user, runtime, st, progress = task
        if 'ERROR' in st:
            bibsched_error = True

    return render_template('inis/bibsched.html', mode=get_bibsched_mode(),
                           tasks=tasks, bibsched_error=bibsched_error, running=running)


@blueprint.route('/list')
@login_required
@register_menu(blueprint, 'main.list', _('Upload List'), order=6,
               visible_when=lambda: current_user.is_admin)
@register_breadcrumb(blueprint, 'breadcrumbs.bibsched', _("Upload List"))
@wash_arguments({'date_from': (unicode, ''),
                 'date_to': (unicode, ''),
                 'issue': (int, 0),
                 'week': (int, 0),
                 'upload_type': (unicode, '')})
def list(date_from, date_to, issue, week, upload_type):

    current_issue, current_week = current_inis_week()

    if week < 1 or issue < 1:
        (issue, week) = (current_issue, current_week)

    if upload_type not in ['', 'INPUT'] and not upload_type.startswith('CAI'):
        upload_type = ''

    date_from, date_to = week_range(issue, week)
    date_from = datetime.combine(date_from, datetime.min.time())
    date_to = datetime.combine(date_to, datetime.max.time())
    week_displayed = (issue, week)
    weeks = []
    issue, week = current_issue, current_week
    weeks.append((current_issue, current_week))
    for i in range(1, 5):
        week = week - 1
        if week == 0:
            week = 50
            issue = issue - 1
        weeks.append((issue, week))

    uploads = get_stats(date_from, date_to, upload_type)

    return render_template('inis/upload_list.html', uploads=uploads, weeks=weeks,
                           week_displayed=week_displayed, upload_type='ALL' if not upload_type else upload_type)


def get_stats(date_from, date_to, upload_type='',
              fields=['id', 'recid', 'action', 'date', 'member', 'submitter',
                      'upload_name', 'notes', 'records', 'files', 'files_no']):
    from inis.utils import get_file_links
    from invenio.modules.deposit.models import Deposition

    if upload_type not in ['', 'INPUT'] and not upload_type.startswith('CAI'):
        upload_type = ''

    uploads = []

    depositions = [d for d in Deposition.get_depositions(date_from=date_from, date_to=date_to) if d.submitted and d.has_sip()]
    depositions = [d for d in depositions if 'action' not in d.get_latest_sip().metadata or d.get_latest_sip().metadata['action'].startswith(upload_type)]
    for d in depositions:
        sip = d.get_latest_sip()
        m = sip.metadata
        if 'Accepted' in m['collections'][0].values():
            u = {}
            if 'id' in fields:
                u['id'] = d.id
            if 'recid' in fields:
                u['recid'] = m['recid']
            if 'action' in fields:
                u['action'] = m['action'] if 'action' in m else ''
            if 'date' in fields:
                u['date'] = str(d.modified)
            if 'member' in fields:
                u['member'] = CFG_MEMBERS_DICT[m['member']]
            if 'submitter' in fields:
                u['submitter'] = m['owner']['username']
            if 'upload_name' in fields:
                u['upload_name'] = d.title
            if 'notes' in fields:
                u['notes'] = m['notes'] if 'notes' in m else None
            if 'records' in fields:
                u['records'] = len(m['trns'])
            if 'files' in fields:
                u['files'] = get_file_links(m['recid'])
            if 'files_no' in fields:
                u['files_no'] = len(m['fft'])

            uploads.append(u)
    return uploads


def current_inis_week():
    today = date.today()

    issue = today.year - 1969
    for w in range(1, 51):
        start, end = week_range(issue, w)
        if start <= today:
            if end >= today:
                return (issue, w)
    issue = issue + 1
    start, end = week_range(issue, 1)
    if start <= today:
        if end >= today:
            return (issue, 1)
    return (0, 0)


def week_range(issue, week_number):

    year = 1969 + issue

    week_offset = min(week_number, 50) - 1
    first_day_year = date(year, 1, 1)
    first_weekday_year = first_day_year.weekday()
    first_wed_year = first_day_year + timedelta(days=2-first_weekday_year)

    if week_number == 1:
        (dummy, start) = week_range(issue-1, 50)
        start = start + timedelta(days=1)
    else:
        start = first_wed_year + timedelta(days=7*week_offset)

    end = first_wed_year + timedelta(days=7*week_offset + 6)

    return (start, end)
