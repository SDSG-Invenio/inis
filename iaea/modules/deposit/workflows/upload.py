from iaea.modules.deposit.forms import UploadForm

from invenio.modules.deposit.tasks import create_recid, \
    finalize_record_sip, \
    prefill_draft, \
    prepare_sip, \
    process_sip_metadata, \
    render_form, \
    upload_record_sip
from invenio.modules.deposit.types import SimpleRecordDeposition


class upload(SimpleRecordDeposition):

    """Upload of batch files  deposit submission."""

    object_type = "submission"

    workflow = [
        # Pre-fill draft with values passed in from request
        prefill_draft(draft_id='default'),
        # Render form and wait for user to submit
        render_form(draft_id='default'),
        # Create the submission information package by merging form data
        # from all drafts (in this case only one draft exists).
        prepare_sip(),
        # Process metadata to match your JSONAlchemy record model. This will
        # call process_sip_metadata() on your subclass.
        process_sip_metadata(),
        # Reserve a new record id, so that we can provide proper feedback to
        # user before the record has been uploaded.
        create_recid(),
        # Generate MARC based on metadata dictionary.
        finalize_record_sip(is_dump=False),
        # Seal the SIP and write MARCXML file and call bibupload on it
        upload_record_sip(),
    ]

    name = "Upload"
    name_plural = "Uploads"
    group = "Articles & Preprints"
    draft_definitions = {
        'default': UploadForm,
    }
