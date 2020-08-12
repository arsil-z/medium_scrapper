import requests
from bs4 import BeautifulSoup


def _get_url_to_fetch_data(string):
	source = requests.get(f'https://medium.com/search?q={string}').text
	return source

def _get_soup(url):
	soup = BeautifulSoup(url, 'lxml')
	return soup


