from webapp.news.models import News
from flask import Blueprint, render_template
from webapp.api_weather import get_weather

blueprint = Blueprint("news", __name__)


@blueprint.route('/')
def index():
    info_about_weather = get_weather()
    news_list = News.query.order_by(News.published.desc()).all()

    weather_in_moscow = 'Погода в Москве'

    return render_template("index.html", weather_in_moscow=weather_in_moscow,
                           news_list=news_list,
                           info_about_weather=info_about_weather)
