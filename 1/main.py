"""Простой парсер WP"""

import requests
from bs4 import BeautifulSoup


def get_html(url):
    """Преобразуем код страницы в текст"""
    my_request = requests.get(url)
    return my_request.text


def get_data(html):
    """Преобразуем html код в дерево объектов python """
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', id='home-welcome').find('header').find('h1').text
    return h1


def main():
    """Получаем код страницы в виде html"""
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__name__':
    main()

main()
