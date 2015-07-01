# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2012, 2013, 2014, 2015 CERN.
#
# Zenodo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this licence, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from inis.utils import id_generator, set_password

from invenio.base.factory import with_app_context
from invenio.ext.sqlalchemy import db


@with_app_context(new_context=True)
def post_handler_database_create(sender, default_data='', *args, **kwargs):
    """Load data after demosite creation."""
    from inis.config import CFG_MEMBERS_NAMES, CFG_ILOS

    from invenio.modules.accounts.models import User, Usergroup, UserUsergroup

    print(">>> Adding user accounts for ILOs.")
    users = {}
    i = 2
    for ilo in CFG_ILOS:
        u = User(id=i, email=ilo['email'], nickname=ilo['name'], password=id_generator())
        db.session.add(u)
        users[ilo['country']] = i
        i = i + 1
    db.session.commit()

    print(">>> Adding user groups for INIS members.")
    for member_name in CFG_MEMBERS_NAMES:
        ug = Usergroup(name=member_name, join_policy='VM', description='Submissions from ' + member_name)
        ug.users.append(UserUsergroup(id_user=1, user_status=UserUsergroup.USER_STATUS['ADMIN']))
        if member_name in users:
            ug.users.append(UserUsergroup(id_user=users[member_name]))
        db.session.add(ug)

    db.session.commit()

    print(">>> Sending password reset to ILOs.")
    for ilo in CFG_ILOS:
        set_password(ilo['email'])

    print(">>> Loading descriptors...")
    print(">>> Relax, this will take a while")

    from inis.demosite.descriptors_en import descriptors_en
    import invenio.modules.knowledge.api as kb
    kb.add_kb('descriptors')
    t = float(len(descriptors_en))
    i = 1
    for d in descriptors_en:
        kb.add_kb_mapping('descriptors', d, d)
        print("\r%d%%" % (i*100/t))
        i += 1
    print(">>> Descriptors loaded successfully!!!")
