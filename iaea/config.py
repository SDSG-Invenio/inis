import sys

CFG_SITE_LANGS = ["en"]

CFG_SITE_NAME = "INIS Input Management"
CFG_SITE_NAME_INTL = {
    "en": CFG_SITE_NAME
}

DEPOSIT_TYPES = [
    "iaea.modules.deposit.workflows.upload:upload",
]

PACKAGES = [
    "iaea.base",
    "iaea.modules.deposit",
    "invenio.modules.*",
    "invenio.base",
]

try:
    from iaea import instance_config
    sys.modules[__name__] = instance_config
    del instance_config
except ImportError:
    pass
