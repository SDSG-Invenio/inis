"""Contains forms related to INIS submissions."""

import os

from datetime import date

from datetime import datetime

from flask import current_app, request

from inis.config import CFG_COUNTRIES_DICT, CFG_LANG_CODES, CFG_MONTH_CODES, CFG_SEASON_CODES
from inis.modules.deposit.field_widgets import BooleanInput, SelectInput

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import ColumnInput, ExtendedListWidget, ItemWidget, plupload_widget

from invenio.modules.deposit.filter_utils import strip_string
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit.validation_utils import required_if

from wtforms import validators
from wtforms.validators import ValidationError


#from . import fields as inisfields

lang_codes_list = CFG_LANG_CODES.items()
lang_codes_list.sort(key=lambda tup: tup[1])

country_codes_list = CFG_COUNTRIES_DICT.items()
country_codes_list.sort(key=lambda tup: tup[1])


class SingleDateForm(WebDepositForm):

    year = fields.SelectField(
        # validators=[validators.DataRequired(message='Publication year is required')],
        default='',
        choices=[('', 'year'), ] + [(str(i), i) for i in reversed(xrange(1900, date.today().year + 1))],
        widget=SelectInput(class_="col-xs-3"),
    )
    month = fields.SelectField(
        label=_("Month or season"),
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
        widget=SelectInput(class_="col-xs-5"),
    )
    day = fields.SelectField(
        default='',
        choices=[('', 'day'), ] + [(str(i), i) for i in xrange(1, 32)],
        widget=SelectInput(class_="col-xs-2"),
    )


class DateForm(WebDepositForm):
    date_from = fields.FormField(
        SingleDateForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label='',
        widget_classes='',
    )
    date_range = fields.BooleanField(
        widget=BooleanInput(class_="col-xs-2"),
        default=False,
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
    # country = fields.StringField(
    #     placeholder="Affiliation country",
    #     widget_classes='form-control',
    #     widget=ColumnInput(class_="col-xs-8"),
    # )
    country = fields.SelectField(
        default='',
        widget=SelectInput(class_="col-xs-8"),
        choices=[('', ''), ] + country_codes_list,
    )


class BookForm(WebDepositForm):
    """INIS record input form fields."""

    #
    # Fields
    #

    #
    # Basic information
    #

    record_type = fields.HiddenField(
        label='',
        default="B",
    )

    trn = fields.StringField(
        label="TRN",
        default='',
        validators=[validators.DataRequired(), ],
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-barcode fa-fw',
        export_key='trn',
    )

    title = fields.TitleField(
        validators=[validators.DataRequired()],
        # description='Required.',
        filters=[
            strip_string,
        ],
        icon='fa fa-book fa-fw',
    )

    original_title = fields.StringField(
        label=_("Original title"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )

    language = fields.DynamicFieldList(
        fields.SelectField(
            validators=[validators.DataRequired()],
            filters=[
                strip_string,
            ],
            default='',
            choices=[('', ''), ('EN', 'English'),
                     ('FR', 'French'), ('DE', 'German'),
                     ('', '------'), ] + lang_codes_list,
            widget=SelectInput(class_="col-xs-3"),
        ),
        add_label='Add another language',
        label=_('Publication Language'),
        icon='fa fa-flag fa-fw',
        validators=[validators.DataRequired()],
        widget_classes='',
        min_entries=1,
        max_entries=8,
    )

    description = fields.TextAreaField(
        label=_("Physical description"),
        validators=[validators.DataRequired()],
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
    )

    #
    # Publication information
    #

    # place = fields.StringField(
    #     label=_("Place of Publication"),
    #     default='',
    #     icon='fa fa-globe fa-fw',
    #     validators=[
    #         required_if(
    #             'familyname',
    #             [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Publication place is required
    #                      if you specify a publisher."
    #         ),
    #     ],
    #     filters=[
    #         strip_string,
    #     ],
    #     widget_classes='form-control',
    # )

    place = fields.FormField(
        LocationForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label=_("Place of Publication"),
        icon='fa fa-globe fa-fw',
        widget_classes='',
    )

    publisher = fields.StringField(
        label=_("Publisher"),
        default='',
        validators=[validators.DataRequired()],
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )

    publication_date = fields.FormField(
        DateForm,
        label=_('Publication date'),
        icon='fa fa-calendar fa-fw',
        widget_classes='',
    )

    # publication_date = fields.SelectField(
    #     label=_('Publication date'),
    #     icon='fa fa-calendar fa-fw',
    #     validators=[validators.DataRequired()],
    #     filters=[
    #         strip_string,
    #     ],
    #     default=0,
    #     choices=[('', ''), ] + CFG_SEASON_CODES +
    #             [(' ', '------'), ] + CFG_MONTH_CODES
    # )

    # publication_date = fields.Date(
    #     label=_('Publication date'),
    #     icon='fa fa-calendar fa-fw',
    #     description='Format: YYYY-MM-DD.',
    #     validators=[validators.DataRequired()],
    #     default=date.today(),
    #     widget=date_widget,
    #     widget_classes='input-sm',
    # )

    edition = fields.StringField(
        label=_("Edition"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )

    #
    # Authors
    #

    creators = fields.DynamicFieldList(
        fields.FormField(
            CreatorForm,
            widget=ExtendedListWidget(
                item_widget=ItemWidget(),
                html_tag='div'
            ),
        ),
        label='Authors',
        add_label='Add another author',
        icon='fa fa-user fa-fw',
        widget_classes='',
        min_entries=1,
        export_key='authors',
    )

    #
    # Conference information
    #

    conference_title = fields.StringField(
        label=_("Conference title"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )
    original_conference_title = fields.StringField(
        label=_("Original conference title"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )

    conference_place = fields.FormField(
        LocationForm,
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label=_("Conference place"),
        icon='fa fa-globe fa-fw',
        widget_classes='',
    )

    conference_date = fields.FormField(
        DateForm,
        label=_('Conference date'),
        icon='fa fa-calendar fa-fw',
        widget_classes='',
    )

    #
    # Identifying numbers
    #

    secondary_number = fields.StringField(
        label=_("Secondary numbers"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )
    isbn = fields.StringField(
        label=_("ISBN/ISSN"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )
    contract_number = fields.StringField(
        label=_("Contract/Project number"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )

    #
    # Extra information
    #

    general_notes = fields.TextAreaField(
        label=_("General notes"),
        # description='Optional.',
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
    )
    availability = fields.StringField(
        label=_("Availability"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )
    title_augmentation = fields.StringField(
        label=_("Title Augmentation"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )
    funding_organization_code = fields.StringField(
        label=_("Funding Organization code"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )
    corporate_entry_code = fields.StringField(
        label=_("Corporate Entry code"),
        default='',
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
    )

    #
    # Form configuration
    #
    _title = _('Book or Monograph')
    _drafting = True   # enable and disable drafting

    #
    # Grouping of fields
    #
    groups = [
        ('Basic information', [
            'trn', 'title', 'original_title', 'language', 'description',
        ], {'indication': 'required', }),
        ('Publication information', [
            'place', 'publisher', 'publication_date', 'edition',
        ], {
            'indication': 'required',
        }),
        ('Authors', [
            'creators',
        ], {
            'classes': '',
            'indication': 'recommended',
        }),
        ('Conference', [
            'conference_title', 'original_conference_title',
            'conference_place', 'conference_date',
        ], {
            'classes': '',
            'indication': 'optional',
        }),
        ('Identifying numbers', [
            'secondary_number', 'isbn', 'contract_number',
        ], {
            'classes': '',
            'indication': 'optional',
        }),
        ('Extra information', [
            'general_notes', 'availability', 'title_augmentation',
            'funding_organization_code', 'corporate_entry_code',
        ], {
            'classes': '',
            'indication': 'optional',
        }),
    ]


class UploadForm(WebDepositForm):
    """INIS record upload form fields."""

    title = fields.TitleField(
        label=_('Upload name'),
        widget_classes="form-control",
        placeholder='e.g. Upload of ' + datetime.now().strftime('%Y-%m-%d %H:%M'),
        icon='fa fa-book fa-fw',
        validators=[validators.DataRequired()],
        export_key='title.title',
    )

    action = fields.RadioField(
        label=_('Action'),
        icon='fa fa-book fa-fw',
        validators=[validators.DataRequired()],
        export_key='action',
        widget_classes='list-unstyled',
        default='INPUT',
        choices=[('INPUT', 'Final input for INIS'),
                 ('CAI', 'To be indexed in CAI')]
    )

    note = fields.TextAreaField(
        label=_("Notes"),
        description='Optional.',
        default='',
        validators=[validators.optional()],
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
        export_key='notes',
        placeholder="e.g. Journal of Radiation Research. JP. 23 records"
    )

    plupload_file = fields.FileUploadField(
        label="",
        widget=plupload_widget,
        export_key=False
    )

    def validate_plupload_file(form, field):
        """Ensure attached files have valid extensions."""
        if not getattr(request, 'is_api_request', False):
            # Tested in API by a separate workflow task.
            if len(form.files) == 0:
                raise ValidationError("You must provide minumim one file")
            for f in form.files:
                if os.path.splitext(f.name)[1] not in current_app.config['DEPOSIT_ACCEPTED_EXTENSIONS']:
                    raise ValidationError("All files must have one of the following extensions :" +
                                          ', '.join(current_app.config['DEPOSIT_ACCEPTED_EXTENSIONS']))
                # if '-' in f.name:
                #     raise ValidationError("The character '-' is forbidden in the file name")

    _title = _("Upload")

    groups = [
        ('Basic information',
            ['title', 'note', 'action']),
    ]
