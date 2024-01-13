from flask import render_template, Blueprint, redirect, url_for, flash
from flask_login import login_required

from webapp import db
from webapp.community.discussions.forms import DiscussionForm
from webapp.community.discussions.models import Discussions
from webapp.utils import get_redirect_target

blueprint = Blueprint("discussions", __name__)


@blueprint.route("/community/discussions/create")
def discussions_page():
    form = DiscussionForm()
    return render_template("discussions.html", form=form)


@blueprint.route("/community/discussions/creating", methods=["POST"])
@login_required
def creating_discussion():
    form = DiscussionForm()
    if form.validate_on_submit():
        new_discussion = Discussions(title=form.title.data, text=form.text.data)
        db.session.add(new_discussion)
        db.session.commit()
        return redirect(get_redirect_target())
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле: {getattr(form, field).label.text} - {error}")
    return redirect(get_redirect_target())