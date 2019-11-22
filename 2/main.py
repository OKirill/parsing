import requests
from bs4 import BeautifulSoup



def get_html(url):
    my_request = requests.get(url)
    return my_request.text





def main():
    pass




if __name__ == '__main__':
    main()