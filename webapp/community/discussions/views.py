from flask import render_template, Blueprint, redirect, flash, url_for
from flask_login import login_required, current_user

from webapp import db
from webapp.community.discussions.forms import DiscussionForm
from webapp.community.discussions.models import Discussions
from webapp.user.models import User
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
        new_discussion = Discussions(title=form.title.data, text=form.text.data, autor=current_user.id)
        db.session.add(new_discussion)
        db.session.commit()
        return redirect(url_for("http://127.0.0.1:5000/community/discussions"))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле: {getattr(form, field).label.text} - {error}")
    return redirect(get_redirect_target())


@blueprint.route("/community/discussions/<int:id>/delete", methods=["POST"])
@login_required
def delete_discussions(id):
    post = Discussions.query.get_or_404(id)
    try:
        db.session.delete(post)
        db.session.commit()
        return redirect("http://127.0.0.1:5000/community")
    except:
        flash("При удалении формы произошла ошибка")


@blueprint.route('/community/discussion/<int:discussion_id>')
def user_discussion(discussion_id):
    user_question = Discussions.query.get(discussion_id)
    user = User.query.get(user_question.autor)
    return render_template("single_discussion.html", user_discussion=user_question, user=user)