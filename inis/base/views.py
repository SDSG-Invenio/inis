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
                 'range': (unicode, 'this_week')})
def list(date_from, date_to, range):

    from invenio.modules.deposit.models import Deposition
    from invenio.modules.formatter import format_record
    from datetime import datetime, timedelta

    ranges = {
        'today': 1,
        'this_week': 7,
        'last_week': 14,
        'last_month': 31,
    }

    days = ranges[range]

    if date_from:
        try:
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
        except:
            now = datetime.now()
            date_from = now - timedelta(days=days)
    else:
        now = datetime.now()
        date_from = now - timedelta(days=days)

    if date_to:
        try:
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
        except:
            date_to = None
    else:
        date_to = None

    uploads = []

    depositions = [d for d in Deposition.get_depositions(date_from=date_from, date_to=date_to) if d.submitted and d.has_sip()]
    for d in depositions:
        sip = d.get_latest_sip()
        m = sip.metadata
        if 'Accepted' in m['collections'][0].values():
            u = {'id': d.id,
                 'recid': m['recid'],
                 'date': d.modified,
                 'member': CFG_MEMBERS_DICT[m['member']],
                 'submitter': m['owner']['username'],
                 'upload_name': d.title,
                 'notes': m['notes'] if 'notes' in m else None,
                 'records': len(m['trns'])}
            uploads.append(u)

    return render_template('inis/upload_list.html', uploads=uploads, format_record=format_record)
