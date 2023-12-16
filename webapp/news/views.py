from webapp.news.models import News
from flask import Blueprint, render_template, abort
from webapp.api_weather import get_weather

blueprint = Blueprint("news", __name__)


@blueprint.route('/')
def index():
    info_about_weather = get_weather()
    news_list = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()

    weather_in_moscow = 'Погода в Москве'

    return render_template("index.html", weather_in_moscow=weather_in_moscow,
                           news_list=news_list,
                           info_about_weather=info_about_weather)


@blueprint.route("/news/<int:news_id>")
def single_news(news_id):
    my_news = News.query.filter(News.id == news_id).first()

    if not my_news:
        abort(404)

    return render_template('single_news.html', page_title=my_news.title, news=my_news)