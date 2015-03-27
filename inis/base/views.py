from flask import Blueprint, current_app, render_template
from flask.ext.breadcrumbs import register_breadcrumb
from flask.ext.login import current_user
from flask.ext.menu import current_menu, register_menu

from invenio.base.i18n import _

blueprint = Blueprint(
    "inis",
    __name__,
    url_prefix="",
    template_folder="templates",  # where your custom templates will go
    static_folder="static"        # where the assets go
)


@blueprint.before_app_first_request
def register_menu_items():
    """Setup menu for INIS Input Management."""
    item = current_menu.submenu('breadcrumbs.inis')
    item.register('', '')

    item = current_menu.submenu("settings.groups")
    item.register(
        'settings.groups', _('INIS Members'), order=1,
        visible_when=lambda: current_user.is_admin
        )
    # item = current_menu.submenu('main')
    # item.register(
    #     'deposit.create', _('Input'), order=2,
    #     endpoint_arguments_constructor=lambda: dict(name='input')
    # )

    def menu_fixup():
        item = current_menu.submenu("main.webdeposit")
        item._text = "Upload"
        item = current_menu.submenu("breadcrumbs.webdeposit")
        item._text = "Upload"

        # Remove items
        item = current_menu.submenu("main")
        item._child_entries.pop('deposit', None)
        item._child_entries.pop('search', None)
        item._child_entries.pop('documentation', None)

        item = current_menu.submenu("settings.workflows")
        item.hide()
        item = current_menu.submenu("settings.applications")
        item.hide()
        item = current_menu.submenu("settings.oauthclient")
        item.hide()

        # item = current_menu.submenu("settings.groups")
        # item._text = "INIS Members"

        # Append function to end of before first request functions, to ensure
        # all menu items have been loaded.
    current_app.before_first_request_funcs.append(menu_fixup)


@blueprint.route('/instructions', methods=['GET', ])
@register_menu(blueprint, 'main.instructions', _('Instructions'), order=4)
@register_breadcrumb(blueprint, 'breadcrumbs.instructions', _("Instructions"))
def instructions():
    return render_template('deposit/instructions.html')
