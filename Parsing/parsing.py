import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://cars.av.by/nissan'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}
HOST = 'https://cars.av.by'
FILE = 'cars.csv'


def safe_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Год выпуска', 'Пробег', 'Цена в BYN', 'Цена в USD', 'Город'])
        for item in items:
            writer.writerow(
                [item['title'], item['link'], item['year'], item['mileage'], item['pricebyn'], item['priceusd'],
                 item['city']])


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_params_4seconds(html):
    soup = BeautifulSoup(html, 'html.parser')
    url = soup.find('a', class_='button button--default').get('href')
    return url.replace('&page=2', '')


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_='paging__text').get_text()
    pages = pages.split('из')[-1]
    newpages = ''
    for letter in pages:
        if letter.isdecimal():
            newpages += letter

    print(int(newpages))
    return int(newpages) // 25 + 1


def get_content(html, first = True):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')
    top = soup.find('div', class_='listing__top')

    cars = []
    if first:
        mileage = top.find('div', class_='listing-top__params').get_text()
        pricebyn = top.find('div', class_='listing-top__price-byn').get_text()
        priceusd = top.find('div', class_='listing-top__price-usd').get_text()
        cars.append({
            'title': top.find('span', class_='link-text').get_text(),
            'link': HOST + top.find('a', class_='listing-top__title-link').get('href'),
            'year': top.find('div', class_='listing-top__params').get_text()[:4],
            'mileage': mileage.replace('\u2009', '').rstrip('\xa0км').split('\xa0км')[-1][2:],
            'pricebyn': pricebyn.replace('\u2009', '').replace('\xa0р.', ''),
            'priceusd': priceusd.replace('≈\xa0', '').replace('\u2009', '').replace('\xa0$', ''),
            'city': top.find('div', class_='listing-top__info-location').get_text(),
        })
    for item in items:
        mileage = item.find('div', class_='listing-item__params').get_text()
        pricebyn = item.find('div', class_='listing-item__price').get_text()
        priceusd = item.find('div', class_='listing-item__priceusd').get_text()
        cars.append({
            'title': item.find('span', class_='link-text').get_text(),
            'link': HOST + item.find('a', class_='listing-item__link').get('href'),
            'year': item.find('div', class_='listing-item__params').get_text()[:4],
            'mileage': mileage.replace('\u2009', '').rstrip('\xa0км').split('\xa0км')[-1],
            'pricebyn': pricebyn.replace('\u2009', '').replace('\xa0р.', ''),
            'priceusd': priceusd.replace('≈\xa0', '').replace('\u2009', '').replace('\xa0$', ''),
            'city': item.find('div', class_='listing-item__location').get_text(),
        })
    # print(cars)
    # print(len(cars))
    return cars


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages = get_pages_count(html.text)
        # print(f'Парсинг страницы 1 из {pages}...')
        # cars.extend(get_content(html.text))
        url = HOST + get_params_4seconds(html.text)
        print(url)
        if pages > 1:
            for page in range(1, pages + 1):
                print(f'Парсинг страницы {page} из {pages}...')
                html = get_html(url, params={'page': page})
                print(html.url)
                cars.extend(get_content(html.text, False))
        #     print(cars)
        #     print(len(cars))
            safe_file(cars, FILE)
            os.startfile(FILE)
    else:
        print('Error')


# print(get_html('https://cars.av.by/filter?brands%5B0%5D%5Bbrand%5D=2521&price_currency=2', params={'page':5}).url)
parse()
