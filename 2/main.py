import requests
from bs4 import BeautifulSoup


def get_html(url):
    my_request = requests.get(url)
    return my_request.text

def refined(s):
    """1,676 total ratings"""
    rating_split = s.split()[0]
    result = rating_split.replace(',', '')
    print(result)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        rating = plugin.find('span', class_='rating-count').find('a').text
        refined(rating)
        #print(rating)

    #return  plugins


def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
