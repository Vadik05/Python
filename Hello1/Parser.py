import requests
from bs4 import BeautifulSoup

URL = 'https://www.avito.ru/sankt-peterburg/avtomobili/s_probegom-ASgBAgICAUSGFMjmAQ?f=ASgBAQICAUSGFMjmAQNA8AoUrIoB5rYNFL63KO62DRTqtyg&radius=300'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 '
                         'Firefox/71.0', 'accept': '*/*'}


def get_html(url, params=None) :
    r = requests.get(url, headers=HEADERS, params=params)
    return r
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class ='na-card-item')

    cars = []
    for item in items:
        cars.append{{
            'title': item.find('div', class ='na-card-name').get.text()
    }}
    print(cars)
def parse():
    html = get_html(URL)
    if html.status_code == 200:
       get_content(html.text)

    else:
        print('Error')


parse()