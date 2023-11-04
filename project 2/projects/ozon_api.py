import requests


headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.888 YaBrowser/23.9.2.888 Yowser/2.5 Safari/537.36'
}

response = requests.get(url='https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=%2FsearchSuggestions%2F%3Ftext%3D%25D0%25BB%25D0%25BE%25D0%25BD%25D0%25B3%25D1%2581%25D0%25BB%25D0%25B8%25D0%25B2%2520%25D0%25B4%25D1%2580%25D0%25B5%25D0%25B9%25D0%25BD%26url%3D%2Fsearch%2F%3Ftext%3D%7Bvalue%7D%26from_global%3Dtrue'
             , headers=headers)

print(response)
