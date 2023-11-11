import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.933 YaBrowser/23.9.3.933 Yowser/2.5'
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
    print(get_info())