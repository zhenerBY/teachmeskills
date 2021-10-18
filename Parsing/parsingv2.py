import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://cars.av.by/eksklyuziv'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}
HOST = 'https://cars.av.by'
HOST2 = 'https://av.by'
FILE = 'cars.csv'


def catalog_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    cars_p = soup.find_all('li', class_='brandsitem brandsitem--primary')
    cars_s = soup.find_all('li', class_='brandsitem brandsitem--secondary')
    # print('hello')
    # print(cars_p)
    catalog = []
    for car in cars_p:
        caar = car.find_next('a').get('href'),
        catalog.extend(caar)
        # print(caar)
        # print(len(cars_p))
    for car in cars_s:
        caar = car.find_next('a').get('href'),
        catalog.extend(caar)
    # print(catalog)
    # print(len(catalog))
    return catalog


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
    print('Найдено', int(newpages), 'автомобилей')
    return int(newpages) // 25 + 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')
    cars = []
    for item in items:
        mileage = item.find('div', class_='listing-item__params').find_next('span').get_text()
        pricebyn = item.find('div', class_='listing-item__price').get_text()
        priceusd = item.find('div', class_='listing-item__priceusd').get_text()
        cars.append({
            'title': item.find('span', class_='link-text').get_text(),
            'link': HOST + item.find('a', class_='listing-item__link').get('href'),
            'year': item.find('div', class_='listing-item__params').get_text()[:4],
            'mileage': mileage.replace('\u2009', '').replace('\xa0км', ''),
            'pricebyn': pricebyn.replace('\u2009', '').replace('\xa0р.', ''),
            'priceusd': priceusd.replace('≈\xa0', '').replace('\u2009', '').replace('\xa0$', ''),
            'city': item.find('div', class_='listing-item__location').get_text(),
        })
    return cars


def parse():
    catalog = catalog_list(get_html(HOST2).text)
    for counter, item in enumerate(catalog):
        print(counter + 1, '-', item)
    choice = int(input('Введите номер для парсинга :'))
    URL = catalog[choice - 1]
    html = get_html(URL)
    if html.status_code == 200:
        cars = []
        pages = get_pages_count(html.text)
        if pages == 1:
            url = URL
            print(f'Парсинг страницы {pages} из {pages}...')
            html = get_html(url)
            print(html.url)
            cars.extend(get_content(html.text))
        if pages > 1:
            url = HOST + get_params_4seconds(html.text)
            for page in range(1, pages + 1):
                print(f'Парсинг страницы {page} из {pages}...')
                html = get_html(url, params={'page': page})
                print(html.url)
                cars.extend(get_content(html.text))
        safe_file(cars, FILE)
        if os.name == 'nt':
            os.startfile(FILE)
        else:
            print('См. файл - cars.csv.')
    else:
        print('Error')


parse()
# catalog_list(get_html(HOST2).text)
