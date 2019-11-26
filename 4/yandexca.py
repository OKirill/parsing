import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:  # 200 ##403 404
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('rambler.csv', 'a') as f:
        writer = csv.writer(f)
        pass


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    tbl = soup.find_all('tr', class_='nZPAY')

    for table in tbl:
        try:
            name = table.find('a', class_="_1QK24 _1mcB-").text

        except:
            name = ''

        try:
            url = table.find('a', class_="_1QK24 _1mcB-").get('href')

        except:
            url = ''

        try:
            visitors = table.find('td', class_='B-LQS _1eMDh _1T3ZY _3DjCd _3zlKH').text

        except:
            visitors = ''

        print(visitors)


def main():
    url = 'https://top100.rambler.ru/navi?categoryId=1064&period=day&sort=popularity&page=1'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
