import requests
from flask import current_app
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "User-Agent" : f"{current_app.config['HEADERS']}"
    }
    try:
        response = requests.get(url=url, headers=headers)
        return response.text

    except Exception:
        return False


def get_info():
    response = get_data(url='https://www.python.org/blogs/')
    try:
        if response:
            result_list = []
            bs = BeautifulSoup(response, 'lxml')
            cards = bs.find('ul', class_='list-recent-posts menu').find_all('li')
            for card in cards:
                title = card.find('a').text
                url = card.find('a')['href']
                date = card.find('p').text
                result_list.append(
                    {
                        "title": title,
                        "url": url,
                        "date": date
                    }
                )
            return result_list

    except Exception:
        return False


if __name__ == "__main__":
    get_info()