# import
import requests
from bs4 import BeautifulSoup
import csv

# specify the url
url = 'http://books.toscrape.com/catalogue/mesaerion-the-best-science-fiction-stories-1800-1849_983/index.html'

# request get
r = requests.get(url)

if r.ok:
    soup = BeautifulSoup(r.text, 'lxml')
    article = soup.find('article', attrs={'class': 'product_page'})
    table = article.find('table', attrs={'class': 'table'})
    tds = table.findAll('td')

    # universal_product_code(upc)
    upc = table.find('td').getText()
    '''print(upc)'''

    # title
    title = article.find('h1').getText()
    '''print(title)'''

    # price_including_tax
    priceInclTax = tds[3].getText()
    '''print(priceInclTax)'''

    # price_excluding_tax
    priceExclTax = tds[2].getText()
    '''print(priceExclTax)'''

    # number_available
    numberAvailable = tds[5].getText().strip('In stock ()')
    '''print(numberAvailable)'''

    # product_description
    p = article.findAll('p')
    productDescription = p[3].getText()
    '''print(productDescription)'''

    # categorie
    li = soup.find('ul', attrs={'class': 'breadcrumb'}).findAll('li')
    category = li[2].getText()
    '''print(category)'''

    # review_rating
    numberReviews = tds[6].getText()
    '''print(numberReviews)'''

    # imageUrl
    imageSource = article.find(
        'div', attrs={'class': 'item'}).find('img')['src']
    imageUrl = 'http://books.toscrape.com/' + imageSource.strip('../..')

# create and write headers to a list
rows = []
rows.append(["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
             "price_excluding_tax", "number_available", "product_description", "categorie", "review_rating", "image_url"])

# write each result to rows
rows.append([url, upc, title, priceInclTax, priceExclTax, numberAvailable,
             productDescription, category, numberReviews, imageUrl])
print(rows)

# Create csv and write rows to output file
with open('extract.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(rows)
