import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = scv.writer(f)
        pass


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', id='currencies').find('tbody').find_all('tr')
    print(len(trs))


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
