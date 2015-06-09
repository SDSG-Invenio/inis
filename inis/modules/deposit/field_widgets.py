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


from wtforms.widgets import CheckboxInput, HTMLString, Select  # html_params,


# def date_widget(field, **kwargs):
#     """Create datepicker widget."""
#     field_id = kwargs.pop('id', field.id)
#     html = [u'<div class="row"><div class="col-xs-5 col-sm-4">'
#             '<input class="datepicker form-control text-center" %s type="text"></div></div>'
#             % html_params(id=field_id, name=field_id, value=field.data or '')]
#     return HTMLString(u''.join(html))


# def date_range(field, **kwargs):
#     """Create date range widget."""
#     field_id = kwargs.pop('id', field.id)
#     html = [u"""<div class="row">
#                   <div class="col-xs-3 col-sm-4">
#                     <input class="form-control text-center" %s type="text">
#                   </div>
#                   <div class="col-xs-3 col-sm-4">
#                     <input class="form-control text-center" %s type="text">
#                   </div>
#                   <div class="col-xs-3 col-sm-4">
#                     <input class="form-control text-center" %s type="text">
#                   </div>
#                 </div>"""
#             % html_params(id=field_id, name=field_id, value=field.data or '')]
#     return HTMLString(u''.join(html))


class WrappedSelect(Select):

    """Widget to wrap text input in further markup."""

    wrapper = '<div>%(field)s</div>'
    wrapped_widget = Select()

    def __init__(self, widget=None, wrapper=None, **kwargs):
        """Initialize wrapped input with widget and wrapper."""
        self.wrapped_widget = widget or self.wrapped_widget
        self.wrapper_args = kwargs
        if wrapper is not None:
            self.wrapper = wrapper

    def __call__(self, field, **kwargs):
        """Render wrapped input."""
        return HTMLString(self.wrapper % dict(
            field=self.wrapped_widget(field, **kwargs),
            **self.wrapper_args
        ))


class SelectInput(WrappedSelect):

    """Specialized column wrapped input."""

    @property
    def wrapper(self):
        """Wrapper template with description support."""
        if 'description' in self.wrapper_args:
            return ('<div class="%(class_)s">%(field)s'
                    '<p class="text-muted field-desc">'
                    '<small>%(description)s</small></p></div>')
        return '<div class="%(class_)s">%(field)s</div>'


class WrappedCheckbox(CheckboxInput):

    """Widget to wrap text input in further markup."""

    wrapper = '<div>%(field)s</div>'
    wrapped_widget = CheckboxInput()

    def __init__(self, widget=None, wrapper=None, **kwargs):
        """Initialize wrapped input with widget and wrapper."""
        self.wrapped_widget = widget or self.wrapped_widget
        self.wrapper_args = kwargs
        if wrapper is not None:
            self.wrapper = wrapper

    def __call__(self, field, **kwargs):
        """Render wrapped input."""
        return HTMLString(self.wrapper % dict(
            field=self.wrapped_widget(field, **kwargs),
            **self.wrapper_args
        ))


class BooleanInput(WrappedCheckbox):

    """Specialized column wrapped input."""

    @property
    def wrapper(self):
        """Wrapper template with description support."""
        if 'description' in self.wrapper_args:
            return ('<div class="%(class_)s">%(field)s'
                    '<p class="text-muted field-desc">'
                    '<small>%(description)s</small></p></div>')
        return '<div class="%(class_)s">%(field)s&nbspRange</div>'
