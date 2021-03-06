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

# from wtforms import RadioField
# from invenio.modules.deposit.field_base import WebDepositField
# from invenio.modules.deposit.field_widgets import InlineListWidget,\
#     BigIconRadioInput

# from invenio.modules.deposit.field import SelectField

from datetime import date

from inis.config import CFG_MONTH_CODES, CFG_SEASON_CODES

from inis.modules.deposit.field_widgets import SelectInput  # , BooleanInput

from inis.utils import get_kb_items

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import ColumnInput, ExtendedListWidget, ItemWidget
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit.validation_utils import required_if

from wtforms import validators

country_codes_list = get_kb_items('countries')
country_codes_list.sort(key=lambda tup: tup[1])


# def data_range_processor(form, field, submit=False, fields=None):
#     form.publication_date.date_range.date_to.flags.hidden = True
#     form.publication_date.date_range.date_to.flags.disabled = True
#     if field.data:
#         form.publication_date.date_range.date_to.flags.hidden = False
#         form.publication_date.date_range.date_to.flags.disabled = False
#     else:
#         form.publication_date.date_range.date_to.flags.hidden = True
#         form.publication_date.date_range.date_to.flags.disabled = True

def single_date_factory(mandatory=False):

    if mandatory:
        validator = [validators.DataRequired(message='Publication year is required'), ]
    else:
        validator = [required_if('month',
                     [lambda x: bool(x.strip()), ],  # non-empty
                     message="Year is required if you specify the month/season."), ]

    class SingleDateForm(WebDepositForm):
        year = fields.SelectField(
            label='',
            validators=validator,
            default='',
            choices=[('', 'year'), ] + [(str(i), i) for i in reversed(xrange(1900, date.today().year + 1))],
            widget=SelectInput(class_="col-xs-3"),
        )
        month = fields.SelectField(
            label='',
            # label=_("Month or season"),
            validators=[
                required_if(
                    'day',
                    [lambda x: bool(x.strip()), ],  # non-empty
                    message="Month is required if you specify the day."
                ),
            ],
            default='',
            choices=[('', 'month/season'), (' ', '------'), ] +
                    [(str(i+21), CFG_SEASON_CODES[i][1]) for i in xrange(0, len(CFG_SEASON_CODES))] +
                    [(' ', '------'), ] + [(str(i+1), CFG_MONTH_CODES[i][1]) for i in xrange(0, len(CFG_MONTH_CODES))],
            widget=SelectInput(class_="col-xs-5"),
        )
        day = fields.SelectField(
            label='',
            default='',
            choices=[('', 'day'), ] + [(str(i), i) for i in xrange(1, 32)],
            widget=SelectInput(class_="col-xs-2"),
        )
    return SingleDateForm


def date_factory(mandatory=False):
    class DateMandatoryForm(WebDepositForm):
        date_from = fields.FormField(
            single_date_factory(mandatory=mandatory),
            widget=ExtendedListWidget(
                item_widget=ItemWidget(),
                html_tag='div'
            ),
            label='',
            widget_classes='',
        )

        date_to = fields.FormField(
            single_date_factory(mandatory=False),
            widget=ExtendedListWidget(
                item_widget=ItemWidget(),
                html_tag='div'
            ),
            label='',
            widget_classes='',
            # hidden=True,
            # disabled=True,
        )
    return DateMandatoryForm


def location_factory(mandatory=False):
    validator = []
    if mandatory:
        validator = [validators.DataRequired(message='City is required'), ]

    class LocationForm(WebDepositForm):
        city = fields.StringField(
            label='City',
            placeholder="City",
            widget_classes='form-control',
            widget=ColumnInput(class_="col-xs-4"),
            validators=validator,
        )
        country = fields.SelectField(
            label=_("Country"),
            validators=[
                required_if(
                    'city',
                    [lambda x: bool(x.strip()), ],  # non-empty
                    message="Country is required if you specify the city."
                ),
            ],
            default='',
            choices=[('', ''), ] + country_codes_list,
            widget=SelectInput(class_="col-xs-5"),
        )
    return LocationForm


class CreatorForm(WebDepositForm):
    givennames = fields.StringField(
        placeholder="Given names",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-10"),
        validators=[
            required_if(
                'familyname',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Given name is required if you specify family names."
            ),
            required_if(
                'email',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Given name is required if you specify the email."
            ),
            required_if(
                'affiliation',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Given name is required if you specify affiliation."
            ),
            required_if(
                'city',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Given name is required \
                         if you specify affiliation city."
            ),
            required_if(
                'country',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Given name is required \
                         if you specify affiliation country."
            ),
        ],
    )
    familyname = fields.StringField(
        placeholder="Family names",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-10"),
        validators=[
            required_if(
                'givennames',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Family name is required if \
                         you specify given names."
            ),
            required_if(
                'email',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Family name is required if \
                         you specify the email."
            ),
            required_if(
                'affiliation',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Family name is required \
                         if you specify affiliation."
            ),
            required_if(
                'city',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Family name is required \
                         if you specify affiliation city."
            ),
            required_if(
                'country',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Family name is required \
                         if you specify affiliation country."
            ),
        ],
    )
    email = fields.StringField(
        placeholder="user@domain.com",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-8"),
        validators=[validators.email(), validators.Optional()],
    )
    affiliation = fields.StringField(
        placeholder="Affiliation",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-8"),
        validators=[
            required_if(
                'city',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Affiliation is required \
                         if you specify affiliation city."
            ),
            required_if(
                'country',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Affiliation is required \
                         if you specify affiliation country."
            ),
        ],
    )
    city = fields.StringField(
        placeholder="Affiliation city",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-8"),
    )

    country = fields.SelectField(
        default='',
        widget=SelectInput(class_="col-xs-8"),
        choices=[('', ''), ] + country_codes_list,
    )
