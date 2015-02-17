import sys

CFG_SITE_LANGS = ["en"]

CFG_SITE_NAME = "INIS Input Management"
CFG_SITE_NAME_INTL = {
    "en": CFG_SITE_NAME
}

DEPOSIT_TYPES = [
    "inis.modules.deposit.workflows.upload:upload",
]

PACKAGES = [
    "inis.base",
    "inis.modules.deposit",
    "invenio.modules.*",
    "invenio.base",
]

try:
    from inis import instance_config
    sys.modules[__name__] = instance_config
    del instance_config
except ImportError:
    pass
