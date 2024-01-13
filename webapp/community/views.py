from flask import Blueprint, render_template

blueprint = Blueprint("community", __name__)


@blueprint.route('/community')
def community_page():
    return render_template("community.html")