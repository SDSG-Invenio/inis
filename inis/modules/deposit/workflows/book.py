from inis.modules.deposit.forms import BookForm
from inis.modules.deposit.workflows import inis_deposition


class book(inis_deposition):
    name = "Book or Monograph"
    name_plural = "Books or Monographs"
    draft_definitions = {
        'default': BookForm,
    }
