# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
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

from invenio.base.i18n import _
from invenio.ext.login import UserInfo
from invenio.modules.accounts.models import Usergroup


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
# @permission_required('usegroups')
def index():
    """List all user groups."""
    import os
    from invenio.legacy.search_engine import perform_request_search
    from operator import itemgetter
    from invenio.modules.deposit.models import Deposition
    from inis.config import CFG_ERROR_MESSAGES

    uid = current_user.get_id()
    current_user.reload()
    # user = User.query.get(uid)

    user = UserInfo(uid)
    if not user.is_admin and user.info['group']:
        user_group_name = user.info['group'][0]
    else:
        user_group_name = ["International Atomic Energy Agency (IAEA)"]
    current_user_group = None
    groups = Usergroup.query.filter().all()
    stats = []
    totals = {}
    totals['total'] = 0
    totals['accepted'] = 0
    totals['rejected'] = 0
    totals['trns'] = 0
    totals['files'] = 0
    totals['errors'] = {}

    for g in groups:
        info = {}
        info['name'] = g.name
        info['users'] = [u.user.nickname for u in g.users if not u.user.has_super_admin_role]
        if len(info['users']):
            info['trns'] = 0
            info['files'] = 0
            info['errors'] = {}
            for u in g.users:
                depositions = Deposition.get_depositions(UserInfo(u.id_user))
                for d in depositions:
                    s = d.get_latest_sip()
                    if s.metadata['errors'] == []:
                        info['trns'] += len(s.metadata['trns'])
                        info['files'] += len([f for f in s.metadata['fft']
                                              if os.path.splitext(f['path'])[1]
                                              in current_app.config['DEPOSIT_ACCEPTED_MD_EXTENSIONS']])
                    else:
                        for e in s.metadata['errors']:
                            if e['code'] in info['errors']:
                                info['errors'][e['code']] += 1
                            else:
                                info['errors'][e['code']] = 1

            totals['files'] += info['files']
            totals['trns'] += info['trns']
            for i in info['errors'].keys():
                if i in totals['errors']:
                    totals['errors'][i] += info['errors'][i]
                else:
                    totals['errors'][i] = info['errors'][i]

            info['errors'] = info['errors'].items()
            info['errors'].sort(key=lambda tup: tup[1], reverse=True)

            info['accepted'] = len(perform_request_search(cc=g.name))
            totals['accepted'] += info['accepted']

            info['rejected'] = len(perform_request_search(cc='r-' + g.name))
            totals['rejected'] += info['rejected']

            info['total'] = info['rejected'] + info['accepted']
            totals['total'] += info['total']

            # if info['accepted'] or info['rejected']:
            stats.append(info)

            if g.name == user_group_name:
                current_user_group = info

    totals['errors'] = totals['errors'].items()
    totals['errors'].sort(key=lambda tup: tup[1], reverse=True)

    stats = sorted(stats, key=itemgetter('trns'), reverse=True)
    top_submitter = stats[0]['trns']
    for g in stats:
        g['activity'] = (g['trns'] * 100) / top_submitter

    for g in stats:
        if g['name'] == user_group_name:
            current_user_group = g
            stats.remove(g)

    return render_template('stats/index.html', stats=stats, totals=totals,
                           current_user_group=current_user_group, error_messages=CFG_ERROR_MESSAGES)
