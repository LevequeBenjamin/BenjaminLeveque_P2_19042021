# import
import requests
from bs4 import BeautifulSoup

# function createBook


def createBook(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    article = soup.find('article', attrs={'class': 'product_page'})
    table = article.find('table', attrs={'class': 'table'})
    tds = table.findAll('td')
    # universal_product_code(upc)
    upc = table.find('td').getText()
    # title
    title = article.find('h1').getText()
    # price_including_tax
    priceInclTax = tds[3].getText()
    # price_excluding_tax
    priceExclTax = tds[2].getText()
    # number_available
    numberAvailable = tds[5].getText().strip('In stock ()')
    # product_description
    p = article.findAll('p')
    productDescription = p[3].getText()
    # categorie
    li = soup.find('ul', attrs={'class': 'breadcrumb'}).findAll('li')
    category = li[2].getText().strip('\n')
    # review_rating
    numberReviews = tds[6].getText()
    # imageUrl
    imageSource = article.find(
        'div', attrs={'class': 'item'}).find('img')['src']
    imageUrl = 'http://books.toscrape.com/' + imageSource.strip('../..')

    return(url, upc, title, priceInclTax, priceExclTax, numberReviews, productDescription, category, numberReviews, imageUrl)
