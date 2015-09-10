"""Contains forms related to INIS submissions."""

import copy
import os

# from datetime import date

from datetime import datetime

from flask import current_app, request

from inis.modules.deposit.field_widgets import SelectInput
from inis.modules.deposit.fields.inis_fields import CreatorForm, date_factory, location_factory

from inis.utils import get_kb_items

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.autocomplete_utils import kb_autocomplete
from invenio.modules.deposit.field_widgets import ExtendedListWidget, ItemWidget, \
    TagInput, TagListWidget, plupload_widget

from invenio.modules.deposit.filter_utils import strip_string
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit.processor_utils import replace_field_data

from invenio.modules.knowledge.api import get_kb_mapping
# from invenio.modules.deposit.validation_utils import required_if
# from invenio.utils.forms import AutocompleteField

from wtforms import validators, widgets
from wtforms.validators import ValidationError
# from wtforms.widgets import TextInput

# from .autocomplete import descriptor_autocomplete


lang_codes_list = get_kb_items('languages')
lang_codes_list.sort(key=lambda tup: tup[1])


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
    description='Required.',
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


def place_factory(mandatory=False):
    place = fields.FormField(
        location_factory(),
        widget=ExtendedListWidget(
            item_widget=ItemWidget(),
            html_tag='div'
        ),
        label=_("Place of Publication"),
        icon='fa fa-globe fa-fw',
        widget_classes='',
    )
    return place
place = place_factory()

publisher = fields.StringField(
    label=_("Publisher"),
    default='',
    filters=[strip_string, ],
    widget_classes='form-control',
)


def publication_date_factory(mandatory=False):
    publication_date = fields.FormField(
        date_factory(mandatory),
        label=_('Publication date'),
        icon='fa fa-calendar fa-fw',
        widget_classes='',
    )
    return publication_date
publication_date = publication_date_factory(False)

edition = fields.StringField(
    label=_("Edition"),
    default='',
    filters=[strip_string, ],
    widget_classes='form-control',
)
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
    location_factory(),
    widget=ExtendedListWidget(
        item_widget=ItemWidget(),
        html_tag='div'
    ),
    label=_("Conference place"),
    icon='fa fa-globe fa-fw',
    widget_classes='',
)
conference_date = fields.FormField(
    date_factory(False),
    label=_('Conference date'),
    icon='fa fa-calendar fa-fw',
    widget_classes='',
)
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
general_notes = fields.TextAreaField(
    label=_("General notes"),
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
abstract = fields.TextAreaField(
    label=_("Abstract"),
    default='',
    filters=[strip_string, ],
    widget_classes='form-control',
    icon='fa fa-pencil fa-fw',
)


#
# Descriptors
#

def descriptor_kb_value(key_name):
    def _getter(field):
        if field.data:
            val = get_kb_mapping('descriptors', str(field.data))
            if val:
                data = descriptors_kb_mapper(val)
                return data['fields'][key_name]
        return ''
    return _getter


def descriptors_kb_mapper(val):
    data = val['value']
    return {
        'value': "%s" % (data),
        'fields': {
            'id': data,
            'descriptor': data,
        }
    }


class DescriptorForm(WebDepositForm):
    id = fields.StringField(
        widget=widgets.HiddenInput(),
        processors=[
            replace_field_data('descriptor', descriptor_kb_value('descriptor')),
        ],
    )
    descriptor = fields.StringField(
        placeholder="Start typing a descriptor...",
        autocomplete_fn=kb_autocomplete(
            'descriptors',
            mapper=descriptors_kb_mapper
        ),
        widget=TagInput(),
        widget_classes='form-control',
    )


proposed_descriptors = fields.DynamicFieldList(
    fields.FormField(
        DescriptorForm,
        widget=ExtendedListWidget(html_tag='div', item_widget=ItemWidget()),
        export_key='proposed_descriptors',
    ),
    widget=TagListWidget(template="{{descriptor}}",
                         html_tag='ul',
                         class_='list-unstyled',
                         ),
    widget_classes=' dynamic-field-list',
    icon='fa fa-tags fa-fw',
    description="Add here the proposed descriptors",
    #validators=[grants_validator],
)


#
# Subjects
#

def subject_kb_value(key_name):
    def _getter(field):
        if field.data:
            val = get_kb_mapping('subjects', str(field.data))
            if val:
                data = subjects_kb_mapper(val)
                return data['fields'][key_name]
        return ''
    return _getter


def subjects_kb_mapper(val):
    data = val['value']
    return {
        'value': "%s" % (data),
        'fields': {
            'id': data[:3],
            'subject': data,
        }
    }


class SubjectForm(WebDepositForm):
    id = fields.StringField(
        widget=widgets.HiddenInput(),
        processors=[
            replace_field_data('subject', subject_kb_value('id')),
        ],
    )
    subject = fields.StringField(
        placeholder="Start typing a subject...",
        autocomplete_fn=kb_autocomplete(
            'subjects',
            mapper=subjects_kb_mapper
        ),
        widget=TagInput(),
        widget_classes='form-control',
    )


subjects = fields.DynamicFieldList(
    fields.FormField(
        SubjectForm,
        widget=ExtendedListWidget(html_tag='div', item_widget=ItemWidget()),
        export_key='subjects',
    ),
    widget=TagListWidget(template="{{subject}}",
                         html_tag='ul',
                         class_='list-unstyled',
                         ),
    widget_classes=' dynamic-field-list',
    icon='fa fa-tags fa-fw',
    description="Add here the subjects",
    export_key='subjects',
    #validators=[grants_validator],
)


groups = [
    ('Basic information', [
        'trn', 'title', 'original_title', 'subjects', 'language',
        'description', 'proposed_descriptors',
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
    ('Abstract', [
        'abstract',
    ], {
        'classes': '',
        'indication': 'recommended',
    }),
]


def mandatory(field):
    field2 = copy.deepcopy(field)
    field2.kwargs['validators'] = [validators.DataRequired()]
    return field2


######################
#       Input        #
######################


class INISForm(WebDepositForm):
    """INIS record input form fields."""

    # Fields

    # Basic information
    record_type = fields.HiddenField(
        label='',
        default="",
    )
    trn = trn
    title = title
    original_title = original_title
    subjects = subjects
    language = language
    description = description
    proposed_descriptors = proposed_descriptors

    # Publication information
    place = place
    publisher = publisher
    publication_date = publication_date
    edition = edition
    creators = creators
    conference_title = conference_title
    original_conference_title = original_conference_title
    conference_place = conference_place
    conference_date = conference_date
    secondary_number = secondary_number
    isbn = isbn
    contract_number = contract_number
    general_notes = general_notes
    availability = availability
    title_augmentation = title_augmentation
    funding_organization_code = funding_organization_code
    corporate_entry_code = corporate_entry_code
    abstract = abstract

    # Form configuration
    _title = ''
    _drafting = True   # enable and disable drafting
    groups = groups


class BookForm(INISForm):
    record_type = fields.HiddenField(label='', default="B", )
    _title = _('Book or Monograph')
    publisher = mandatory(publisher)


class AudiovisualForm(INISForm):
    record_type = fields.HiddenField(label='', default="F", )
    _title = _('Audiovisual Material')


class MiscellaneousForm(INISForm):
    record_type = fields.HiddenField(label='', default="I", )
    _title = _('Miscellaneous')


class PatentForm(INISForm):
    record_type = fields.HiddenField(label='', default="P", )
    _title = _('Patent')
    conference_title = None
    conference_place = None
    conference_date = None
    original_conference_title = None
    edition = None
    groups = [e for e in groups if e[0] != 'Conference']


class ReportForm(INISForm):
    record_type = fields.HiddenField(label='', default="R", )
    _title = _('Report')
    edition = None
    corporate_entry_code = mandatory(corporate_entry_code)


class ComputerForm(INISForm):
    record_type = fields.HiddenField(label='', default="T", )
    _title = _('ComputerMedia')
    conference_title = None
    conference_place = None
    conference_date = None
    original_conference_title = None
    groups = [e for e in groups if e[0] != 'Conference']


######################
#       Upload       #
######################


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
