"""Contains forms related to INIS submissions."""

import os
from datetime import date

from datetime import datetime

from flask import current_app, request

from inis.utils import filter_empty_helper

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import CKEditorWidget, \
    ColumnInput, ExtendedListWidget, ItemWidget, date_widget, plupload_widget

from invenio.modules.deposit.filter_utils import sanitize_html, strip_string
from invenio.modules.deposit.form import WebDepositForm
from invenio.modules.deposit.processor_utils import PidNormalize
from invenio.modules.deposit.validation_utils import list_length, required_if
from invenio.utils.html import CFG_HTML_BUFFER_ALLOWED_TAG_WHITELIST

from wtforms import validators, widgets
from wtforms.validators import ValidationError


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
    # upload_type = zfields.UploadTypeField(
    #     validators=[validators.DataRequired()],
    #     export_key='upload_type.type',
    # )
    publication_type = fields.SelectField(
        label='Type of publication',
        choices=[
            ('book', 'Book'),
            ('section', 'Book section'),
            ('conferencepaper', 'Conference paper'),
            ('article', 'Journal article'),
            ('patent', 'Patent'),
            ('preprint', 'Preprint'),
            ('proposal', 'Proposal'),
            ('report', 'Report'),
            ('softwaredocumentation', 'Software documentation'),
            ('thesis', 'Thesis'),
            ('technicalnote', 'Technical note'),
            ('workingpaper', 'Working paper'),
            ('other', 'Other'),
        ],
        validators=[
            required_if('upload_type', ['publication']),
            validators.optional()
        ],
        hidden=True,
        disabled=True,
        export_key='upload_type.subtype',
    )
    image_type = fields.SelectField(
        choices=[
            ('figure', 'Figure'),
            ('plot', 'Plot'),
            ('drawing', 'Drawing'),
            ('diagram', 'Diagram'),
            ('photo', 'Photo'),
            ('other', 'Other'),
        ],
        validators=[
            required_if('upload_type', ['image']),
            validators.optional()
        ],
        hidden=True,
        disabled=True,
        export_key='upload_type.subtype',
    )

    #
    # Basic information
    #
    # doi = fields.DOIField(
    #     label="Digital Object Identifier",
    #     description="Optional. Did your publisher already assign a DOI to your"
    #     " upload? If not, leave the field empty and we will register a new"
    #     " DOI for you. A DOI allows others to easily and unambiguously cite"
    #     " your upload.",
    #     placeholder="e.g. 10.1234/foo.bar...",
    #     validators=[
    #         DOISyntaxValidator(),
    #         pre_reserved_doi_validator(
    #             'prereserve_doi',
    #             prefix=CFG_DATACITE_DOI_PREFIX
    #         ),
    #         invalid_doi_prefix_validator(prefix=CFG_DATACITE_DOI_PREFIX),
    #     ],
    #     processors=[
    #         local_datacite_lookup
    #     ],
    #     export_key='doi',
    #     icon='fa fa-barcode fa-fw',
    # )
    # prereserve_doi = zfields.ReserveDOIField(
    #     label="",
    #     doi_field="doi",
    #     doi_creator=create_doi,
    #     widget=ButtonWidget(
    #         label=_("Pre-reserve DOI"),
    #         icon='fa fa-barcode',
    #         tooltip=_(
    #             'Pre-reserve a Digital Object Identifier for your upload. This'
    #             ' allows you know the DOI before you submit your upload, and'
    #             ' can thus include it in e.g. publications. The DOI is not'
    #             ' finally registered until submit your upload.'
    #         ),
    #     ),
    # )
    publication_date = fields.Date(
        label=_('Publication date'),
        icon='fa fa-calendar fa-fw',
        description='Required. Format: YYYY-MM-DD. In case your upload '
        'was already published elsewhere, please use the date of first'
        ' publication.',
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
        export_key='title',
        icon='fa fa-book fa-fw',
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
    description = fields.TextAreaField(
        label="Description",
        description='Required.',
        default='',
        icon='fa fa-pencil fa-fw',
        validators=[validators.DataRequired(), ],
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
        label='Keywords',
        add_label='Add another keyword',
        icon='fa fa-tags fa-fw',
        widget_classes='',
        min_entries=1,
    )
    notes = fields.TextAreaField(
        label="Additional notes",
        description='Optional.',
        default='',
        validators=[validators.optional()],
        filters=[
            strip_string,
        ],
        widget_classes='form-control',
        icon='fa fa-pencil fa-fw',
    )

    #
    # Access rights
    #
    # access_right = zfields.AccessRightField(
    #     label="Access right",
    #     description="Required. Open access uploads have considerably higher "
    #     "visibility on %s." % CFG_SITE_NAME,
    #     default="open",
    #     validators=[validators.DataRequired()]
    # )
    embargo_date = fields.Date(
        label=_('Embargo date'),
        icon='fa fa-calendar fa-fw',
        description='Required only for Embargoed Access uploads. Format: '
        'YYYY-MM-DD. The date your upload will be made publicly available '
        'in case it is under an embargo period from your publisher.',
        default=date.today(),
        validators=[
            required_if('access_right', ['embargoed']),
            validators.optional()
        ],
        widget=date_widget,
        widget_classes='input-small',
        hidden=True,
        disabled=True,
    )
    # license = zfields.LicenseField(
    #     validators=[
    #         required_if('access_right', ['embargoed', 'open', ]),
    #         validators.DataRequired()
    #     ],
    #     default='cc-zero',
    #     domain_data=True,
    #     domain_content=True,
    #     domain_software=True,
    #     description='Required. The selected license applies to all of your '
    #     'files displayed in the bottom of the form. If you want to upload '
    #     'some files under a different license, please do so in two separate'
    #     ' uploads. If you think a license missing is in the list, please '
    #     'inform us at %s.' % CFG_SITE_SUPPORT_EMAIL,
    #     filters=[
    #         strip_string,
    #     ],
    #     placeholder="Start typing a license name or abbreviation...",
    #     icon='fa fa-certificate fa-fw',
    # )
    access_conditions = fields.TextAreaField(
        label=_('Conditions'),
        icon='fa fa-pencil fa-fw',
        description='Specify the conditions under which you grant users '
                    'access to the files in your upload. User requesting '
                    'access will be asked to justify how they fulfil the '
                    'conditions. Based on the justification, you decide '
                    'who to grant/deny access. You are not allowed to '
                    'charge users for granting access to data hosted on '
                    'Zenodo.',
        default="",
        validators=[
            required_if('access_right', ['restricted']),
            validators.optional()
        ],
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
        hidden=True,
        disabled=True,
    )

    #
    # Collection
    #
    # communities = fields.DynamicFieldList(
    #     fields.FormField(
    #         CommunityForm,
    #         widget=ExtendedListWidget(html_tag=None, item_widget=ItemWidget())
    #     ),
    #     validators=[community_validator],
    #     widget=TagListWidget(template="{{title}}"),
    #     widget_classes=' dynamic-field-list',
    #     icon='fa fa-group fa-fw',
    #     export_key='provisional_communities',
    # )

    #
    # Funding
    #
    # grants = fields.DynamicFieldList(
    #     fields.FormField(
    #         GrantForm,
    #         widget=ExtendedListWidget(html_tag=None, item_widget=ItemWidget()),
    #         export_key=lambda f: {
    #             'identifier': f.data['id'],
    #             'title': "%s - %s (%s)" % (
    #                 f.data['acronym'], f.data['title'], f.data['id']
    #             )
    #         }
    #     ),
    #     widget=TagListWidget(template="{{acronym}} - {{title}} ({{id}})"),
    #     widget_classes=' dynamic-field-list',
    #     icon='fa fa-money fa-fw',
    #     description="Optional. Note, a human %s curator will validate your"
    #                 " upload before reporting it to OpenAIRE, and you may "
    #                 "thus experience a delay before your upload is available "
    #                 "in OpenAIRE." % CFG_SITE_NAME,
    #     validators=[grants_validator],
    # )

    #
    # Related work
    #
    # related_identifiers = fields.DynamicFieldList(
    #     fields.FormField(
    #         RelatedIdentifierForm,
    #         description="Optional. Format: e.g. 10.1234/foo.bar",
    #         widget=ExtendedListWidget(
    #             item_widget=ItemWidget(),
    #             html_tag='div'
    #         ),
    #     ),
    #     label="Related identifiers",
    #     add_label='Add another related identifier',
    #     icon='fa fa-barcode fa-fw',
    #     widget_classes='',
    #     min_entries=1,
    # )

    # #
    # # Journal
    # #
    # journal_title = fields.StringField(
    #     label="Journal title",
    #     description="Optional.",
    #     validators=[
    #         required_if(
    #             'journal_volume', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Journal title is required if you specify either "
    #                     "volume, issue or pages."
    #         ),
    #         required_if(
    #             'journal_issue', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Journal title is required if you specify either "
    #                     "volume, issue or pages."
    #         ),
    #         required_if(
    #             'journal_pages', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Journal title is required if you specify either "
    #                     "volume, issue or pages."
    #         ),
    #     ],
    #     export_key='journal.title',
    # )
    # journal_volume = fields.StringField(
    #     label="Volume", description="Optional.", export_key='journal.volume',
    # )
    # journal_issue = fields.StringField(
    #     label="Issue", description="Optional.", export_key='journal.issue',
    # )
    # journal_pages = fields.StringField(
    #     label="Pages", description="Optional.", export_key='journal.pages',
    # )

    # #
    # # Book/report/chapter
    # #
    # partof_title = fields.StringField(
    #     label="Book title",
    #     description="Optional. "
    #                 "Title of the book or report which this "
    #                 "upload is part of.",
    #     export_key='part_of.title',
    # )
    # partof_pages = fields.StringField(
    #     label="Pages",
    #     description="Optional.",
    #     export_key='part_of.pages',
    # )

    # imprint_isbn = fields.StringField(
    #     label="ISBN",
    #     description="Optional.",
    #     placeholder="e.g 0-06-251587-X",
    #     export_key='isbn',
    # )
    # imprint_publisher = fields.StringField(
    #     label="Publisher",
    #     description="Optional.",
    #     export_key='imprint.publisher',
    # )
    # imprint_place = fields.StringField(
    #     label="Place",
    #     description="Optional.",
    #     placeholder="e.g city, country...",
    #     export_key='imprint.place',
    # )

    # #
    # # Thesis
    # #
    # thesis_supervisors = fields.DynamicFieldList(
    #     fields.FormField(
    #         CreatorForm,
    #         widget=ExtendedListWidget(
    #             item_widget=ItemWidget(),
    #             html_tag='div'
    #         ),
    #     ),
    #     label='Supervisors',
    #     add_label='Add another supervisor',
    #     icon='fa fa-user fa-fw',
    #     widget_classes='',
    #     min_entries=1,
    # )
    # thesis_university = fields.StringField(
    #     description="Optional.",
    #     label='Awarding University',
    #     validators=[validators.optional()],
    #     icon='fa fa-building fa-fw',
    # )

    # #
    # # Conference
    # #
    # conference_title = fields.StringField(
    #     label="Conference title",
    #     description="Optional.",
    #     validators=[
    #         not_required_if('conference_acronym', [lambda x: bool(x.strip())]),
    #         required_if(
    #             'conference_dates', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Conference title or acronym is required if you "
    #                     "specify either dates or place."
    #         ),
    #         required_if(
    #             'conference_place', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Conference title or acronym is required if you "
    #                     "specify either dates or place."
    #         ),
    #     ],
    #     export_key="meetings.title"
    # )
    # conference_acronym = fields.StringField(
    #     label="Acronym",
    #     description="Optional.",
    #     validators=[
    #         not_required_if('conference_title', [lambda x: bool(x.strip())]),
    #         required_if(
    #             'conference_dates', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Conference title or acronym is required if you "
    #                     "specify either dates or place."
    #         ),
    #         required_if(
    #             'conference_place', [lambda x: bool(x.strip()), ],  # non-empty
    #             message="Conference title or acronym is required if you "
    #                     "specify either dates or place."
    #         ),
    #     ],
    #     export_key="meetings.acronym",
    # )
    # conference_dates = fields.StringField(
    #     label="Dates", description="Optional.",
    #     placeholder="e.g 21-22 November 2012...",
    #     export_key="meetings.dates",
    # )
    # conference_place = fields.StringField(
    #     label="Place",
    #     description="Optional.",
    #     placeholder="e.g city, country...",
    #     export_key="meetings.place",
    # )
    # conference_url = fields.StringField(
    #     label="Website",
    #     description="Optional. E.g. http://zenodo.org",
    #     validators=[validators.optional(), validators.URL()]
    # )
    # conference_session = fields.StringField(
    #     label="Session",
    #     description="Optional. Number of session within the conference.",
    #     placeholder="e.g VI",
    #     export_key="meetings.session",
    # )
    # conference_session_part = fields.StringField(
    #     label="Part",
    #     description="Optional. Number of part within a session.",
    #     placeholder="e.g 1",
    #     export_key="meetings.session_part",
    # )

    #
    # References
    #
    # references = zfields.TextAreaListField(
    #     label="References",
    #     description="Optional. Format: One reference per line.",
    #     validators=[validators.optional(), ],
    #     icon='fa fa-bookmark',
    #     placeholder="One reference per line...",
    # )

    #
    # File upload field
    #
    plupload_file = fields.FileUploadField(
        label="",
        widget=plupload_widget,
        export_key=False
    )

    def validate_plupload_file(form, field):
        """Ensure minimum one file is attached."""
        if not getattr(request, 'is_api_request', False):
            # Tested in API by a separate workflow task.
            if len(form.files) == 0:
                raise ValidationError("You must provide minimum one file.")

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
            'doi', 'prereserve_doi', 'publication_date', 'title',  'creators', 'description',
            'keywords', 'notes',
        ], {'indication': 'required', }),
        # ('Journal', [
        #     'journal_title', 'journal_volume', 'journal_issue',
        #     'journal_pages',
        # ], {
        #     'classes': '',
        #     'indication': 'optional',
        # }),
        # ('Conference', [
        #     'conference_title', 'conference_acronym', 'conference_dates',
        #     'conference_place', 'conference_url', '-', 'conference_session',
        #     'conference_session_part'
        # ], {
        #     'classes': '',
        #     'indication': 'optional',
        # }),
        # ('Book/Report/Chapter', [
        #     'imprint_publisher',  'imprint_place', 'imprint_isbn', '-',
        #     'partof_title', 'partof_pages',
        # ], {'classes': '', 'indication': 'optional', }),
        # ('Thesis', [
        #     'thesis_university', 'thesis_supervisors',
        # ], {
        #     'classes': '',
        #     'indication': 'optional',
        # }),
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
