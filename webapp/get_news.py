import requests
from bs4 import BeautifulSoup
from datetime import datetime
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


def get_info():
    dates = {
        "Dec": "12",
        "Nov": "11",
        "Oct": "10",
        "Sep": "9",
        "Aug": "8",
        "Jul": "7",
        "Jun": "6",
        "May": "5",
        "Apr": "4",
        "Mar": "3",
        "Feb": "2",
        "Jan": "1",
    }
    response = get_data(url='https://www.python.org/blogs/')
    try:
        if response:
            bs = BeautifulSoup(response, 'lxml')
            cards = bs.find('ul', class_='list-recent-posts menu').find_all('li')
            for card in cards:
                title = card.find('a').text
                url = card.find('a')['href']
                published = card.find('time').text
                published = f"{published.split('.')[1].split(',')[1].strip()}-" \
                            f"{dates[published.split('.')[0]].strip()}-" \
                            f"{published.split('.')[1].split(',')[0].strip()}"
                published = published.replace(' ', '-')
                try:
                    published = datetime.strptime(published, '%Y-%m-%d')
                except ValueError:
                    published = datetime.now()
                save_news(title, url, published)

    except Exception:
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
