from flask import render_template, Blueprint, redirect, flash, url_for, request
from flask_login import login_required, current_user

from webapp import db
from webapp.community.discussions.forms import DiscussionForm, AnswerForm
from webapp.community.discussions.models import Discussions, Answers
from webapp.user.models import User
from webapp.utils import get_redirect_target
from datetime import datetime

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
        return redirect(url_for("community.community_page"))
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
        flash("При удалении вопроса произошла ошибка")


@blueprint.route("/community/discussions/<int:discussion_id>/update", methods=["POST", "GET"])
@login_required
def update_discussion(discussion_id):
    discussion = Discussions.query.get_or_404(discussion_id)
    if request.method == "POST":
        form = DiscussionForm()
        if form.validate_on_submit():
            discussion.title = form.title.data
            discussion.text = form.text.data
            try:
                db.session.commit()
            except:
                flash("Произошла ошибка")
            return redirect(url_for("community.community_page"))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Ошибка в поле: {getattr(form, field).label.text} - {error}")
    else:
        form = DiscussionForm()
        form.text.data = discussion.text
        return render_template("discussions_update.html", discussion_id=discussion_id, form=form,
                               discussion=discussion)


@blueprint.route('/community/discussion/<int:discussion_id>')
def user_discussion(discussion_id):
    user_question = Discussions.query.get(discussion_id)
    user = User.query.get(user_question.autor)

    form = AnswerForm(id_discussion=user_question.id)
    form.id_discussion.data = discussion_id

    answers = Answers.query.filter_by(discussion_id=discussion_id).order_by(Answers.date.asc()).all()
    answers_json = []
    for answer in answers:
        answers_json.append(
            {
                "id": answer.id,
                "text": answer.text,
                "date": answer.date,
                "user_id": answer.user_id,
                "discussion_id": answer.discussion_id,
                "username": User.query.get(answer.user_id).username
            }
        )

    return render_template("single_discussion.html", user_discussion=user_question, user=user,
                           form=form, discussion_id=form.id_discussion.data,
                           answers=answers_json)


@blueprint.route("/community/discussions/add-answer", methods=["POST"])
@login_required
def add_answer():
    form = AnswerForm()
    if form.validate_on_submit():
        if Discussions.query.filter(Discussions.id == form.id_discussion.data).first():
            new_answer = Answers(text=form.text.data, user_id=current_user.id, discussion_id=form.id_discussion.data,
                                 date=datetime.now())
            db.session.add(new_answer)
            db.session.commit()
            flash("Ответ успешно добавлен")
            return redirect(get_redirect_target() or url_for("discussions.user_discussion",
                                                             discussion_id=form.id_discussion.data))

    return redirect(get_redirect_target() or url_for("discussions.user_discussion"))


@blueprint.route("/profile/<int:id>")
def profile(id):
    discussions = Discussions.query.filter(Discussions.autor == id).all()
    discussions_json = []
    posts_count = Discussions.query.filter(Discussions.autor == id).count()
    for discussion in discussions:
        discussions_json.append(
            {
                "title": discussion.title,
                "url": f"http://127.0.0.1:5000/community/discussion/{discussion.id}",
            }
        )
    return render_template("profile.html", discussions_json=discussions_json, posts_count=posts_count)