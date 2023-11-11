from flask import Flask, render_template

from webapp.model import db, News
from webapp.api_weather import get_weather

"""set FLASK_APP=webapp && set FLASK_ENV=development && set DEBUG=1 && flask run """


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        info_about_weather = get_weather()
        news_list = News.query.order_by(News.published.desc()).all()

        title = "Новостной сайт"
        weather_in_moscow = 'Погода в Москве'

        return render_template("index.html", page_title=title, weather_in_moscow=weather_in_moscow,
                               news_list=news_list,
                               info_about_weather=info_about_weather)
    return app
