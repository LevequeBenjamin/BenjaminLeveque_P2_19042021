# import
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import numpy as np
from book import createBook
from bookLink import scrapBookLink
from categoryLink import scrapCategoryLink


rows = []
rows.append(["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
             "price_excluding_tax", "number_available", "product_description", "categorie", "review_rating", "image_url"])
# specify the url
url = 'http://books.toscrape.com/index.html'
categoryLink = scrapCategoryLink(url)


def allLinkPage():
    for i in range(21):
        url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + \
            str(i) + '.html'
        bookLink = scrapBookLink(url)
    return bookLink


bookLink = allLinkPage()


def allBook(bookLink):
    for i in range(len(bookLink)):
        r = requests.get(bookLink[i])
        book = createBook(bookLink[i])

        # write each result to rows
        rows.append([book])


allBook(bookLink)

# Create csv and write dict
with open('extract.csv', 'w+') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(rows)
