"""Contains forms related to INIS submissions."""

import os

# from datetime import date

from datetime import datetime

from flask import current_app, request

from inis.config import CFG_LANG_CODES

from inis.modules.deposit.field_widgets import SelectInput
from inis.modules.deposit.fields.inis_fields import CreatorForm, DateMandatoryForm, DateOptionalForm, LocationForm

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import ExtendedListWidget, ItemWidget, plupload_widget

from invenio.modules.deposit.filter_utils import strip_string
from invenio.modules.deposit.form import WebDepositForm
# from invenio.modules.deposit.validation_utils import required_if

from wtforms import validators
from wtforms.validators import ValidationError

lang_codes_list = CFG_LANG_CODES.items()
lang_codes_list.sort(key=lambda tup: tup[1])


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
        filters=[strip_string, ],
        widget_classes='form-control',
        icon='fa fa-barcode fa-fw',
        export_key='trn',
    )

    title = fields.TitleField(
        validators=[validators.DataRequired()],
        # description='Required.',
        filters=[strip_string, ],
        icon='fa fa-book fa-fw',
    )

    original_title = fields.StringField(
        label=_("Original title"),
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
    )

    language = fields.DynamicFieldList(
        fields.SelectField(
            validators=[validators.DataRequired()],
            filters=[strip_string, ],
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
        filters=[strip_string, ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
    )

    #
    # Publication information
    #

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
        filters=[strip_string, ],
        widget_classes='form-control',
    )

    publication_date = fields.FormField(
        DateMandatoryForm,
        label=_('Publication date'),
        icon='fa fa-calendar fa-fw',
        widget_classes='',
    )

    edition = fields.StringField(
        label=_("Edition"),
        default='',
        filters=[strip_string, ],
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
        filters=[strip_string, ],
        widget_classes='form-control',
    )
    original_conference_title = fields.StringField(
        label=_("Original conference title"),
        default='',
        filters=[strip_string, ],
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
        DateOptionalForm,
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
        filters=[strip_string, ],
        widget_classes='form-control',
    )
    isbn = fields.StringField(
        label=_("ISBN/ISSN"),
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
    )
    contract_number = fields.StringField(
        label=_("Contract/Project number"),
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
    )

    #
    # Extra information
    #

    general_notes = fields.TextAreaField(
        label=_("General notes"),
        # description='Optional.',
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
    )
    availability = fields.StringField(
        label=_("Availability"),
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
    )
    title_augmentation = fields.StringField(
        label=_("Title Augmentation"),
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
    )
    funding_organization_code = fields.StringField(
        label=_("Funding Organization code"),
        default='',
        filters=[strip_string, ],
        widget_classes='form-control',
    )
    corporate_entry_code = fields.StringField(
        label=_("Corporate Entry code"),
        default='',
        filters=[strip_string, ],
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
        filters=[strip_string, ],
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
