# -*- coding: utf-8 -*-
import sys

CFG_SITE_LANGS = ["en"]

CFG_SITE_NAME = "INIS Input Management"
CFG_SITE_NAME_INTL = {
    "en": CFG_SITE_NAME
}

DEPOSIT_TYPES = [
    "inis.modules.deposit.workflows.upload:upload",
    "inis.modules.deposit.workflows.book:book",
    "inis.modules.deposit.workflows.audiovisual:audiovisual",
    "inis.modules.deposit.workflows.miscellaneous:miscellaneous",
    "inis.modules.deposit.workflows.report:report",
    "inis.modules.deposit.workflows.patent:patent",
    "inis.modules.deposit.workflows.computer:computer",
]

PACKAGES = [
    "inis.base",
    "inis.demosite",
    "inis.modules.deposit",
    "inis.modules.formatter",
    "inis.modules.stats",
    "invenio.modules.*",
    "invenio.base",
]

try:
    from inis import instance_config
    sys.modules[__name__] = instance_config
    del instance_config
except ImportError:
    pass

CFG_ERROR_MESSAGES = {
    0: 'Fulltext files have names that do not correspond to any known TRN',
    1: 'Files do not contain TTF metadata (or TRN tag "001" is missing)',
    2: 'Wrong country code in TRNs',
    3: 'Duplicated TRNs',
}

CFG_SUMBISSION_ERRORS = {
    0: 'The following fulltext files have names that do not correspond to any known TRN:',
    1: 'The following files do not contain TTF metadata (or TRN tag "001" is missing):',
    2: 'The following TRNs have the wrong country code:',
    3: 'The following TRNs are duplicated (or tag "009" is nor "C" for change record):',
}

CFG_NOTIFY_SUBMISSION = ['d.mironov@iaea.org', 'j.garcia-llopis@iaea.org']

CFG_BIBINDEX_PATH_TO_STOPWORDS_FILE = "etc/bibrank/stopwords.kb"

CFG_OAI_METADATA_FORMATS = {
    'oai_dc': ('XOAIDC', 'http://www.openarchives.org/OAI/1.1/dc.xsd',
                         'http://purl.org/dc/elements/1.1/'),
    'oai_ttf': ('XOAITTF', '', ''),
    'marcxml': ('XOAIMARC',
                'http://www.loc.gov/standards/marcxml/schema/MARC21slim.xsd',
                'http://www.loc.gov/MARC21/slim'),
    }

CFG_ILOS = [
    {'country': 'International Atomic Energy Agency (IAEA)', 'name': 'Alexander Anastassov', 'email': 'a.Anastassov@iaea.org'},
    {'country': 'Spain', 'name': 'Jaime García', 'email': 'j.garcia-llopis@iaea.org'},
]

CFG_MONTH_CODES = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
]
CFG_SEASON_CODES = [
    ('Spr', 'Spring'),
    ('Sum', 'Summer'),
    ('Aut', 'Autum'),
    ('Win', 'Winter'),
]

CFG_RECORD_TYPES = {
    'B': "Book or Monograph",
    'F': "Audiovisual Material",
    'I': "Miscellaneous",
    'P': "Patent",
    'R': "Report",
    'T': "Computer Media",
}
