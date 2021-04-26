# import libraries
import requests
from bs4 import BeautifulSoup


# query the website and return the html to the variable 'res'
# parse the html using beautiful soup and store in variable 'soup'
def get_data(url: str) -> BeautifulSoup:
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup
