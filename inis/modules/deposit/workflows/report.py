from inis.modules.deposit.forms import ReportForm
from inis.modules.deposit.workflows import inis_deposition


class report(inis_deposition):
    name = "Report"
    name_plural = name + 's'
    draft_definitions = {
        'default': ReportForm,
    }
