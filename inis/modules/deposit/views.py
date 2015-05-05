"""
Base blueprint for INIS Input Management
"""

from __future__ import absolute_import

from flask import Blueprint


blueprint = Blueprint(
    'inis_deposit',
    __name__,
    static_folder="static",
    # template_folder="templates",
)
