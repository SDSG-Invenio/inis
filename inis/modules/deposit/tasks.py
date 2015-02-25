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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""INIS workflow tasks."""

from functools import wraps

from invenio.modules.deposit.models import Deposition


#
# Workflow tasks
#
def check_files():
    """Check if ttf and txt files look like TTF metadata."""
    @wraps(check_files)
    def _check_files(obj, eng):
        d = Deposition(obj)
        sip = d.get_latest_sip(sealed=False)
        if sip is None:
            sip = d.create_sip()

        f = open('/tmp/log', 'w')
        f.write(str(sip.metadata['fft']) + '\n')
        f.close()

    return _check_files
