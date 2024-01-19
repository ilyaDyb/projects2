from webapp.news.models import News, Comment
from webapp.user.models import User
from flask import Blueprint, flash, redirect, render_template, abort
from webapp.api_weather import get_weather
from webapp.news.forms import CommentForm, GetSubscribe
from flask_login import current_user, login_required
from webapp.db import db
from webapp.utils import get_redirect_target

blueprint = Blueprint("news", __name__)


@blueprint.route('/')
def index():
    info_about_weather = get_weather()
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()

    weather_in_moscow = 'Погода в Москве'
    subscribe_form = GetSubscribe()

    return render_template("index.html", weather_in_moscow=weather_in_moscow,
                           news_list=news_list,
                           info_about_weather=info_about_weather,
                           subscribe_form=subscribe_form,
                           user_id=current_user.id)


@blueprint.route("/news/<int:news_id>")
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()

    if not my_news:
        abort(404)
    comment_form = CommentForm(news_id=my_news.id)
    return render_template('single_news.html', page_title=my_news.title, news=my_news, comment_form=comment_form)


@blueprint.route("/news/comment", methods=['POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(text=form.comment_text.data, news_id=form.news_id.data, user_id=current_user.id)
        db.session.add(comment)
        db.session.commit()
        flash("Comment has been added")
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле: {getattr(form, field).label.text} - {error}")
    return redirect(get_redirect_target())


@blueprint.route("/news/subscribe", methods=['POST'])
@login_required
def add_subscribe():
    form = GetSubscribe()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        user.role = 'subscriber'
        db.session.commit()
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Ошибка в поле: {getattr(form, field).label.text} - {error}")

    return redirect(get_redirect_target())