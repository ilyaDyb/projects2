from bs4 import BeautifulSoup
import locale
import platform
from datetime import datetime
from webapp.news.models import News
from webapp import db

from webapp.news.pasers.utils import get_data, save_news

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'russian')
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')


def get_info_from_habr():
    response = get_data(url='https://habr.com/ru/search/?target_type=posts&q=python&order_by=date')
    correct_format = '%Y-%m-%d %H:%M'
    if response:
        bs = BeautifulSoup(response, 'lxml')
        cards = bs.find('div', class_='tm-articles-list').find_all('article', class_='tm-articles-list__item')
        for card in cards:
            title = card.find('h2', class_='tm-title tm-title_h2').text
            url = f"https://habr.com{card.find('h2').find('a')['href']}"
            published = card.find('time').get('title')
            published = f"{published.replace(',', '')}"
            published = datetime.strptime(published, correct_format)

            save_news(title, url, published)


def get_content_from_habr():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        response = get_data(news.url)
        if response:
            bs = BeautifulSoup(response, "lxml")
            news_text = bs.find('div', id='post-content-body').decode_contents()
            if news_text:
                news.text = news_text
                db.session.add(news)
                db.session.commit()

