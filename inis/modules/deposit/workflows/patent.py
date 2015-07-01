from inis.modules.deposit.forms import PatentForm
from inis.modules.deposit.workflows import inis_deposition


class patent(inis_deposition):
    name = "Patent"
    name_plural = name + 's'
    draft_definitions = {
        'default': PatentForm,
    }
