# from datetime import datetime

from inis.config import CFG_MEMBERS_INV

from inis.modules.deposit.forms import UploadForm
from inis.modules.deposit.tasks import create_error_message, \
    file_names_not_in_TRNs, get_TRNs, get_duplicated_trns, \
    notify_rejection, validate

from invenio.ext.login import UserInfo

from invenio.modules.deposit.tasks import create_recid, \
    finalize_record_sip, \
    prefill_draft, \
    prepare_sip, \
    process_sip_metadata, \
    render_form, \
    upload_record_sip
from invenio.modules.deposit.types import SimpleRecordDeposition


from workflow import patterns as p


def process_recjson(deposition, recjson):
    try:
        sip = deposition.get_latest_sip(sealed=False)
        if sip is None:
            sip = deposition.create_sip()

        user = UserInfo(deposition.user_id)
        if not user.is_admin:
            recjson['member'] = CFG_MEMBERS_INV[user.info['group'][0]]
        else:
            recjson['member'] = CFG_MEMBERS_INV["International Atomic Energy Agency (IAEA)"]
        recjson['errors'] = []

        TRNs = get_TRNs(sip)
        recjson['trns'] = TRNs

        wrong_cc = [trn for trn in TRNs if trn[:2] != recjson['member']]
        if wrong_cc != [] and recjson['member'] != 'XA':
            sip.metadata['errors'].append({'code': 2, 'list': wrong_cc})

        missing_trns = file_names_not_in_TRNs(sip)
        recjson['missing_trns'] = missing_trns
        if missing_trns != []:
            sip.metadata['errors'].append({'code': 0, 'list': missing_trns})

        duplicated_trns = get_duplicated_trns(sip)
        recjson['duplicated_trns'] = duplicated_trns
        if duplicated_trns != []:
            sip.metadata['errors'].append({'code': 3, 'list': duplicated_trns})

        if recjson['errors']:
            primary = 'Rejected'
        else:
            primary = 'Accepted'

        recjson['collections'] = [{'primary': primary, 'secondary': recjson['member']}, ]

        error_message = create_error_message(sip)
        sip.metadata['error_message'] = error_message

    except TypeError:
        # Happens on re-run
        pass

    return recjson


def process_recjson_new(deposition, recjson):
    """
    Process exported recjson for a new record
    """
    process_recjson(deposition, recjson)

    # ================
    # Owner
    # ================
    # Owner of record (can edit/view the record)
    user = UserInfo(deposition.user_id)
    email = user.info.get('email', '')
    recjson['owner'] = dict(
        email=email,
        username=user.info.get('nickname', ''),
        id=deposition.user_id,
        deposition_id=deposition.id,
    )

    return recjson


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
        process_sip_metadata(process_recjson_new),
        # Reserve a new record id, so that we can provide proper feedback to
        # user before the record has been uploaded.
        create_recid(),
        # Generate MARC based on metadata dictionary.
        finalize_record_sip(is_dump=False),
        # Check files
        p.IF_ELSE(
            validate(),
            [
                upload_record_sip(),
            ],
            [
                notify_rejection(),
                upload_record_sip(),
            ]
        ),
    ]

    name = "Upload"
    name_plural = "Uploads"
    group = "INIS Submissions"
    draft_definitions = {
        'default': UploadForm,
    }
