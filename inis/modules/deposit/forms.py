"""Contains forms related to INIS submissions."""

import os
from datetime import date

from datetime import datetime

from flask import current_app, request

from inis.config import CFG_LANG_CODES
from inis.modules.deposit.field_widgets import date_widget
from inis.utils import filter_empty_helper

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import CKEditorWidget, \
    ColumnInput, ExtendedListWidget, ItemWidget, plupload_widget

from invenio.modules.deposit.filter_utils import sanitize_html, strip_string
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit.processor_utils import PidNormalize
from invenio.modules.deposit.validation_utils import list_length, required_if
from invenio.utils.html import CFG_HTML_BUFFER_ALLOWED_TAG_WHITELIST

from wtforms import validators, widgets
from wtforms.validators import ValidationError

lang_codes_list = CFG_LANG_CODES.items()
lang_codes_list.sort(key=lambda tup: tup[1])


class CreatorForm(WebDepositForm):
    name = fields.StringField(
        placeholder="Family name, First name",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-6"),
        validators=[
            required_if(
                'affiliation',
                [lambda x: bool(x.strip()), ],  # non-empty
                message="Creator name is required if you specify affiliation."
            ),
        ],
    )
    affiliation = fields.StringField(
        placeholder="Affiliation",
        widget_classes='form-control',
        widget=ColumnInput(class_="col-xs-4 col-pad-0"),
    )
    orcid = fields.StringField(
        widget=widgets.HiddenInput(),
        processors=[
            PidNormalize(scheme='orcid'),
        ],
    )

    def validate_orcid(form, field):
        if field.data:
            from invenio.utils import persistentid
            schemes = persistentid.detect_identifier_schemes(
                field.data or ''
            )
            if 'orcid' not in schemes:
                raise ValidationError("Not a valid ORCID-identifier.")


class InputForm(WebDepositForm):
    """INIS record input form fields."""

    #
    # Fields
    #
    trn = fields.StringField(
        label=_("TRN"),
        description='Required.',
        default='',
        validators=[validators.DataRequired(), ],
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-barcode fa-fw',
        export_key='trn',
    )
    publication_date = fields.Date(
        label=_('Publication date'),
        icon='fa fa-calendar fa-fw',
        description='Required. Format: YYYY-MM-DD. '
        'Please use the date of first publication.',
        default=date.today(),
        validators=[validators.DataRequired()],
        widget=date_widget,
        widget_classes='input-sm',
    )
    title = fields.TitleField(
        validators=[validators.DataRequired()],
        description='Required.',
        filters=[
            strip_string,
        ],
        export_key='title.title',
        icon='fa fa-book fa-fw',
    )
    language = fields.SelectField(
        label=_('Language'),
        validators=[validators.DataRequired()],
        description='Required.',
        filters=[
            strip_string,
        ],
        default=0,
        choices=[('', ''), ('EN', 'English'), ('FR', 'French'), ('DE', 'German'),
                 ('', '------'), ] + lang_codes_list,
        icon='fa fa-flag fa-fw',
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
        validators=[validators.DataRequired(), list_length(
            min_num=1, element_filter=filter_empty_helper(),
        )],
    )
    abstract = fields.TextAreaField(
        label="Abstract",
        # description='Required.',
        default='',
        icon='fa fa-pencil fa-fw',
        # validators=[validators.DataRequired(), ],
        widget=CKEditorWidget(
            toolbar=[
                ['PasteText', 'PasteFromWord'],
                ['Bold', 'Italic', 'Strike', '-',
                 'Subscript', 'Superscript', ],
                ['NumberedList', 'BulletedList', 'Blockquote'],
                ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'RemoveFormat'],
                ['Mathjax', 'SpecialChar', 'ScientificChar'], ['Source'],
                ['Maximize'],
            ],
            disableNativeSpellChecker=False,
            extraPlugins='scientificchar,mathjax,blockquote',
            removePlugins='elementspath',
            removeButtons='',
            # Must be set, otherwise MathJax tries to include MathJax via the
            # http on CDN instead of https.
            mathJaxLib='https://cdn.mathjax.org/mathjax/latest/MathJax.js?'
                       'config=TeX-AMS-MML_HTMLorMML'
        ),
        filters=[
            sanitize_html(allowed_tag_whitelist=(
                CFG_HTML_BUFFER_ALLOWED_TAG_WHITELIST + ('span',)
            )),
            strip_string,
        ],
    )
    keywords = fields.DynamicFieldList(
        fields.StringField(
            widget_classes='form-control',
            widget=ColumnInput(class_="col-xs-10"),
        ),
        label='Descriptors',
        add_label='Add another descriptor',
        icon='fa fa-tags fa-fw',
        widget_classes='',
        min_entries=1,
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
    )

    #
    # File upload field
    #
    plupload_file = fields.FileUploadField(
        label="",
        widget=plupload_widget,
        export_key=False
    )

    def validate_plupload_file(form, field):
        """Ensure attached files have valid extensions."""
        if not getattr(request, 'is_api_request', False):
            # Tested in API by a separate workflow task.
            for f in form.files:
                if os.path.splitext(f.name)[1] not in current_app.config['DEPOSIT_ACCEPTED_EXTENSIONS']:
                    raise ValidationError("All files must have one of the following extensions :" +
                                          ', '.join(current_app.config['DEPOSIT_ACCEPTED_EXTENSIONS']))
                if '-' in f.name:
                    raise ValidationError("The character '-' is forbidden in the file name")

    #
    # Form configuration
    #
    _title = _('New record')
    _drafting = True   # enable and disable drafting

    #
    # Grouping of fields
    #
    groups = [
        ('Basic information', [
            'trn', 'title', 'language', 'publication_date', 'creators',
        ], {'indication': 'required', }),
        ('Extra information', [
            'abstract', 'keywords', 'note',
        ], {
            'classes': '',
            'indication': 'recommended',
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
