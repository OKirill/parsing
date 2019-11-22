import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    """вытягиваем из url html"""
    my_request = requests.get(url)
    return my_request.text


def refined(s):
    """1,676 total ratings"""
    rating_split = s.split()[0]
    return rating_split.replace(',', '')


def write_csv(data):
    """Запись результатов парсинга в cvs файл"""
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))


def get_data(html):
    """преобразуем html в python """
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        rate = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(rate)

        data = {'name': name,
                'url': url,
                'reviews': rating}

        # print(data)
        write_csv(data)


def main():
    """обрабатываем url"""
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
