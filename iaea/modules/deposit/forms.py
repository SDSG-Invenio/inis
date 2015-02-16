"""Contains forms related to INIS submissions."""

from invenio.base.i18n import _

from invenio.modules.deposit import fields
from invenio.modules.deposit.filter_utils import strip_string
from invenio.modules.deposit.form import WebDepositForm

from wtforms import validators


class UploadForm(WebDepositForm):
    """INIS record upload form fields."""

    title = fields.TitleField(
        label=_('Title'),
        widget_classes="form-control",
        export_key='title.title',
    )

    note = fields.TextAreaField(
        label="Additional notes",
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

    _title = _("Upload")

    groups = [
        ('Basic information',
            ['title', 'note']),
    ]
