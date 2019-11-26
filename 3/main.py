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


def main():
    pass


if __name__ == '__main__':
    main()
