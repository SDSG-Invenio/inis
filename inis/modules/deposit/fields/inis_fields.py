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

from datetime import date

from inis.config import CFG_COUNTRIES_DICT, CFG_MONTH_CODES, CFG_SEASON_CODES

from inis.modules.deposit.field_widgets import BooleanInput, SelectInput

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import ColumnInput, ExtendedListWidget, ItemWidget
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit.validation_utils import required_if

from wtforms import validators

country_codes_list = CFG_COUNTRIES_DICT.items()
country_codes_list.sort(key=lambda tup: tup[1])


def data_range_processor(form, field, submit=False, fields=None):
    form.publication_date.date_range.date_to.flags.hidden = True
    form.publication_date.date_range.date_to.flags.disabled = True
    if field.data:
        form.publication_date.date_range.date_to.flags.hidden = False
        form.publication_date.date_range.date_to.flags.disabled = False
    else:
        form.publication_date.date_range.date_to.flags.hidden = True
        form.publication_date.date_range.date_to.flags.disabled = True


class SingleDateForm(WebDepositForm):
    year = fields.SelectField(
        label='',
        validators=[required_if('month',
                    [lambda x: bool(x.strip()), ],  # non-empty
                    message="Year is required if you specify the month/season."),
                    ],
        default='',
        choices=[('', 'year'), ] + [(str(i), i) for i in reversed(xrange(1900, date.today().year + 1))],
        widget=SelectInput(class_="col-xs-2"),
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
        choices=[('', 'month/season'), (' ', '------'), ] + CFG_SEASON_CODES +
                [(' ', '------'), ] + CFG_MONTH_CODES,
        widget=SelectInput(class_="col-xs-4"),
    )
    day = fields.SelectField(
        label='',
        default='',
        choices=[('', 'day'), ] + [(str(i), i) for i in xrange(1, 32)],
        widget=SelectInput(class_="col-xs-2"),
    )


class SingleDateRangeForm(SingleDateForm):
    date_range = fields.BooleanField(
        label='',
        description=_("Range"),
        widget=BooleanInput(class_="col-xs-3"),
        default=False,
    )


class SingleDateMandatoryForm(SingleDateForm):
    def __iter__(self):
        """ Iterate form fields in their order of definition on the form. """
        for name in self.fields_order:
            if name in self._fields:
                yield self._fields[name]
    year = fields.SelectField(
        label='',
        validators=[validators.DataRequired(message='Publication year is required'), ],
        default='',
        choices=[('', 'year'), ] + [(str(i), i) for i in reversed(xrange(1900, date.today().year + 1))],
        widget=SelectInput(class_="col-xs-2"),
    )
    date_range = fields.BooleanField(
        label='',
        description=("Range"),
        widget=BooleanInput(class_="col-xs-3"),
        default=False,
    )
    fields_order = ('year', 'month', 'day', 'date_range')


class DateMandatoryForm(WebDepositForm):
    date_from = fields.FormField(
        SingleDateMandatoryForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label='',
        widget_classes='',
    )

    date_to = fields.FormField(
        SingleDateForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label='',
        widget_classes='',
        hidden=True,
        disabled=True,
    )


class DateOptionalForm(WebDepositForm):
    date_from = fields.FormField(
        SingleDateRangeForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label='',
        widget_classes='',
    )

    date_to = fields.FormField(
        SingleDateForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label='',
        widget_classes='',
        hidden=True,
        disabled=True,
    )


class LocationForm(WebDepositForm):
    city = fields.StringField(
        label='City',
        placeholder="City",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-4"),
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
