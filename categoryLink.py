# import
import requests
from bs4 import BeautifulSoup
categoryLinks = []
# function createBook


def scrapCategoryLink(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    lis = soup.find('ul', attrs={'class': 'nav-list'}).findAll('li')
    for li in lis:
        categoryLink = li.find('a')['href']
        categoryLink = 'http://books.toscrape.com/' + \
            categoryLink.strip('/index.html')
        categoryLinks.append(categoryLink)
    return categoryLinks
