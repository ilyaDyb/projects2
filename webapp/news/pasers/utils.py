import requests


from webapp.news.models import News
from webapp.db import db


def get_data(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5'
                      '845.933 YaBrowser/23.9.3.933 Yowser/2.5'
    }
    try:
        response = requests.get(url=url, headers=headers)
        return response.text

    except Exception:
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
