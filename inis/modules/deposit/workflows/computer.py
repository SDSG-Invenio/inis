from inis.modules.deposit.forms import ComputerForm
from inis.modules.deposit.workflows import inis_deposition


class computer(inis_deposition):
    name = "Computer Media"
    name_plural = name + 's'
    draft_definitions = {
        'default': ComputerForm,
    }
