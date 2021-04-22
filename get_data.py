# import
import requests
from bs4 import BeautifulSoup

def get_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup