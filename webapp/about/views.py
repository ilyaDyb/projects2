from flask import Blueprint, render_template


blueprint = Blueprint("about", __name__)


@blueprint.route("/info")
def info_page():
    return render_template("info_page.html")