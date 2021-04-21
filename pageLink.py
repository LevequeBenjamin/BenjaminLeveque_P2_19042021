# import
import requests
from bs4 import BeautifulSoup

# function scrapPageLink
def scrapPageLink(url):
    links = []
    # request get
    r = requests.get(url)
    if r.ok:

        soup = BeautifulSoup(r.text, 'lxml')
        articles = soup.findAll('article', attrs={'class': 'product_pod'})

        for article in articles:
            link = article.find('a')['href']
            link = 'http://books.toscrape.com/catalogue/' + \
                link.strip('../../..')
            links.append(link)
    return(links)
