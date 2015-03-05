"""Contains forms related to INIS submissions."""

import os

from flask import current_app, request

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.field_widgets import plupload_widget
from invenio.modules.deposit.filter_utils import strip_string
from invenio.modules.deposit.form import WebDepositForm

from wtforms import validators
from wtforms.validators import ValidationError


class UploadForm(WebDepositForm):
    """INIS record upload form fields."""

    title = fields.TitleField(
        label=_('Title'),
        description='Optional.',
        widget_classes="form-control",
        icon='fa fa-book fa-fw',
        validators=[validators.DataRequired()],
        export_key='title.title',
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

    _title = _("Upload")

    groups = [
        ('Basic information',
            ['title', 'note']),
    ]
