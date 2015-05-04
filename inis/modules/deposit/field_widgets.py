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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Implement custom field widgets."""


from wtforms.widgets import HTMLString, html_params


def date_widget(field, **kwargs):
    """Create datepicker widget."""
    field_id = kwargs.pop('id', field.id)
    html = [u'<div class="row"><div class="col-xs-5 col-sm-4">'
            '<input class="datepicker form-control text-center" %s type="text"></div></div'
            % html_params(id=field_id, name=field_id, value=field.data or '')]
    return HTMLString(u''.join(html))
