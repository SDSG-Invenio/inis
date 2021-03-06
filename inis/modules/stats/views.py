# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014, 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Stats Flask Blueprint."""

from flask import Blueprint, current_app, render_template
from flask.ext.breadcrumbs import default_breadcrumb_root, register_breadcrumb
from flask.ext.login import current_user, login_required
from flask.ext.menu import register_menu

from inis.utils import get_kb_key, get_kb_value

from invenio.base.i18n import _
from invenio.ext.login import UserInfo
from invenio.ext.principal import permission_required
from invenio.modules.accounts.models import Usergroup
from invenio.modules.deposit.models import Deposition


blueprint = Blueprint(
    'stats',
    __name__,
    url_prefix="/stats",
    template_folder='templates',
    static_folder='static'
)

default_breadcrumb_root(blueprint, '.settings.stats')


@blueprint.route('/')
@blueprint.route('/index')
@register_menu(
    blueprint, 'settings.stats',
    _('%(icon)s Statistics', icon='<i class="fa fa-bar-chart-o fa-fw"></i>'),
    # visible_when=lambda: current_user.is_admin
)
#     active_when=lambda: request.endpoint.startswith("webgroup.")
# )
@register_breadcrumb(blueprint, '.', _('Statistics'))
@login_required
@permission_required('usegroups')
def index():
    """List all user groups."""
    from operator import itemgetter
    from inis.config import CFG_ERROR_MESSAGES

    uid = current_user.get_id()
    current_user.reload()
    # user = User.query.get(uid)

    user = UserInfo(uid)

    if not user.is_authorized('viewstatistics') and user.info['group']:
        user_group_name = user.info['group'][0]
        info = get_group_stats(user_group_name)
        return render_template('stats/member.html', info=info, error_messages=CFG_ERROR_MESSAGES)

    else:
        user_group_name = ["International Atomic Energy Agency (IAEA)"]

        depositions = [d for d in Deposition.get_depositions() if d.state == 'done']
        members = set()
        for d in depositions:
            s = d.get_latest_sip()
            members.add(s.metadata['member'])

        stats = []
        totals = {}
        totals['total'] = 0
        totals['accepted'] = 0
        totals['rejected'] = 0
        totals['trns'] = 0
        totals['files'] = 0
        totals['batches'] = 0
        totals['errors'] = {}

        for code in members:
            info = get_group_stats(get_kb_value('members', code))
            if info['accepted'] or info['rejected']:
                stats.append(info)
                totals['files'] += info['files']
                totals['batches'] += info['batches']
                totals['trns'] += info['trns']
                errors = dict(info['errors'])
                for i in errors.keys():
                    if i in totals['errors']:
                        totals['errors'][i] += errors[i]
                    else:
                        totals['errors'][i] = errors[i]

                totals['accepted'] += info['accepted']
                totals['rejected'] += info['rejected']
                totals['total'] += info['total']

        totals['errors'] = totals['errors'].items()
        totals['errors'].sort(key=lambda tup: tup[1], reverse=True)

        stats = sorted(stats, key=itemgetter('name'), reverse=False)

        return render_template('stats/global.html', stats=stats, totals=totals, error_messages=CFG_ERROR_MESSAGES)


@blueprint.route('/<int:id_usergroup>')
@login_required
@permission_required('usegroups')
def member_stats(id_usergroup):
    """Display statistics for one member."""
    from inis.config import CFG_ERROR_MESSAGES

    g = Usergroup.query.filter_by(id=id_usergroup).first()
    info = get_group_stats(g.name)

    return render_template('stats/member.html', info=info, error_messages=CFG_ERROR_MESSAGES)


def get_group_stats(group_name):
    import os
    from invenio.legacy.search_engine import perform_request_search

    g = Usergroup.query.filter_by(name=group_name).first()
    iaea_group = Usergroup.query.filter_by(name='International Atomic Energy Agency (IAEA)').first()

    member = get_kb_key('members', g.name)
    info = {}
    info['name'] = group_name
    info['id'] = str(g.id)
    info['users'] = [u.user.nickname for u in g.users if not u.user.has_super_admin_role]
    info['trns'] = 0
    info['files'] = 0
    info['batches'] = 0
    info['errors'] = {}

    for u in set(g.users + iaea_group.users):
        # if not u.is_admin() or group_name == "International Atomic Energy Agency (IAEA)":
        depositions = Deposition.get_depositions(UserInfo(u.id_user))
        for d in depositions:
            if d.has_sip() and d.state == 'done':
                s = d.get_latest_sip()
                if s.metadata['member'] == member:
                    if s.metadata['errors'] == []:
                        info['trns'] += len(s.metadata['trns'])
                        info['files'] += len([f for f in s.metadata['fft']
                                              if os.path.splitext(f['path'])[1]
                                              in current_app.config['DEPOSIT_ACCEPTED_FULLTEXT_EXTENSIONS']])
                        info['batches'] += len([f for f in s.metadata['fft']
                                                if os.path.splitext(f['path'])[1]
                                                in current_app.config['DEPOSIT_ACCEPTED_MD_EXTENSIONS']])
                    else:
                        for e in s.metadata['errors']:
                            if e['code'] in info['errors']:
                                info['errors'][e['code']] += 1
                            else:
                                info['errors'][e['code']] = 1

    info['errors'] = info['errors'].items()
    info['errors'].sort(key=lambda tup: tup[1], reverse=True)
    info['accepted'] = len(perform_request_search(cc=member))
    info['rejected'] = len(perform_request_search(cc='r-' + member))
    info['total'] = info['rejected'] + info['accepted']

    return info
