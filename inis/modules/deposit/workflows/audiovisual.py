from inis.modules.deposit.forms import AudiovisualForm
from inis.modules.deposit.workflows import inis_deposition


class audiovisual(inis_deposition):
    name = "Audiovisual Material"
    name_plural = name + 's'
    draft_definitions = {
        'default': AudiovisualForm,
    }
