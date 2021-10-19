import requests
from bs4 import BeautifulSoup
import csv
import os

HOST = 'https://myfin.by/'
URL = 'https://myfin.by/kredity/potrebitelskie'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
FILE = 'kredity.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_contect(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products-table__body-item-wrapper')
    kredit = []
    for item in items:
        try:
            persent = item.find('span', class_='accent').get_text()
        except AttributeError:
            persent = 'по согласованию'
        kredit.append({
            'persent': persent,
            'title': item.find('div', class_='products-table__body-item-logo').find('img').get('alt'),
            'link': HOST + item.find('div', class_='products-table__body-item-name').find('a').get('href'),
            'summ': item.find('div', class_='products-table__body-item-data-2').get_text(strip=True),
            'period': item.find('div', class_='products-table__body-item-data-3').get_text(strip=True)
        })
    return kredit


def save_pars(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['bank', 'persent', 'summ', 'period', 'link'])
        for item in items:
            writer.writerow([item['title'], item['persent'], item['summ'], item['period'], item['link']])


def pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='pagination-new pagination-new--v2 text-center')
    items = items.find_all('li')
    pages = set()
    for item in items:
        if item.find('a'):
            if str(item.find('a').get('href')[-1]).isnumeric():
                pages.add(int(item.find('a').get('href')[-1]))
    return max(pages)


def parsing():
    html = get_html(URL)
    PAGE = pages(html.text)
    if html.status_code == 200:
        kredit = []
        for page in range(1, PAGE + 1):
            print(f'парсинг {page}')
            html = get_html(URL, params={'page': page})
            kredit.extend(get_contect(html.text))
        print(f'получено {len(kredit)} предложений')
        save_pars(kredit, FILE)
        os.startfile(FILE)
    else:
        print('no answer from server')


parsing()
