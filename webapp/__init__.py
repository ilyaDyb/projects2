from flask import Flask, render_template

from webapp.api_weather import get_weather
from webapp.get_news import get_info
"""set FLASK_APP=webapp && set FLASK_ENV=development && DEBUG=1 && flask run """


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        info_about_weather = get_weather()
        news_list = get_info()

        title = "Новостной сайт"
        weather_in_moscow = 'Погода в Москве'

        return render_template("index.html", page_title=title, weather_in_moscow=weather_in_moscow,
                               news_list=news_list,
                               info_about_weather=info_about_weather)
    return app
