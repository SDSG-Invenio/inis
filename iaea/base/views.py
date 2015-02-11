from flask import Blueprint

blueprint = Blueprint(
    "iaea",
    __name__,
    url_prefix="/",
    template_folder="templates",  # where your custom templates will go
    static_folder="static"        # where the assets go
)
