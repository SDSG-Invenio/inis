# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2012, 2013 CERN.
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

# from wtforms import RadioField
# from invenio.modules.deposit.field_base import WebDepositField
# from invenio.modules.deposit.field_widgets import InlineListWidget,\
#     BigIconRadioInput

# from invenio.modules.deposit.field import SelectField


def data_range_processor(form, field, submit=False, fields=None):
    form.publication_date.date_range.date_to.flags.hidden = True
    form.publication_date.date_range.date_to.flags.disabled = True
    if field.data:
        form.publication_date.date_range.date_to.flags.hidden = False
        form.publication_date.date_range.date_to.flags.disabled = False
    else:
        form.publication_date.date_range.date_to.flags.hidden = True
        form.publication_date.date_range.date_to.flags.disabled = True


# def set_license_processor(form, field, submit=False, fields=None):
#     # Only run license processor, when the license wasn't specified.
#     if fields and 'license' not in fields:
#         if field.data == "dataset":
#             if not form.license.flags.touched:
#                 form.license.data = 'cc-zero'
#         elif field.data == "software":
#             if not form.license.flags.touched:
#                 form.license.data = 'mit-license'
#         else:
#             if not form.license.flags.touched:
#                 form.license.data = 'cc-by'


# class UploadTypeField(WebDepositField, SelectField):

#     """
#     Field to render a list
#     """
#     widget = InlineListWidget()
#     option_widget = SelectField()

#     def __init__(self, **kwargs):
#         kwargs['choices'] = [(x[0], x[1]) for x in UPLOAD_TYPES]
#         kwargs['processors'] = [
#             data_range_processor,
#         ]

#         super(UploadTypeField, self).__init__(**kwargs)
