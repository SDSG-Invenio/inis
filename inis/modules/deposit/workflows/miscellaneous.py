from inis.modules.deposit.forms import MiscellaneousForm
from inis.modules.deposit.workflows import inis_deposition


class miscellaneous(inis_deposition):
    name = "Miscellaneous"
    name_plural = name
    draft_definitions = {
        'default': MiscellaneousForm,
    }
