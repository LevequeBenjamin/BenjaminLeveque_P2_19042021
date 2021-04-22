# import
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from book import createBook
from bookLink import scrapBookLink
from categoryLink import scrapCategoryLink
from save_csv import save_book_info_to_csv
import csv


rows = []


# specify the url
# url = 'http://books.toscrape.com/index.html'
# url_category = scrapCategoryLink(url)

# categorie_url = url de la page d'accueil de la catégorie
# Tant qu'il y a un bouton next faire et donc que categorie_url n'est pas vide
#     urls = récupérer les urls des livres de la page
#     Pour chaque url dans url faire:
#          scraper et sauvegarder les infos du livre correspondant à l'url
#     Fin pour
#     categorie_url = url de la prochaine page si le bouton next existe sinon ''
# Fin tant que
url = 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html'
def get_data(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.content, 'html.parser')
  return soup

def get_next_page(soup):
  page = soup.find('ul', attrs={'class': 'pager'})
  if page.find('li', attrs={'class': 'next'}):
    url = 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/' + str(page.find('li', attrs={'class': 'next'}).find('a')['href'])
    return url
  else:
    return

while True:
  soup = get_data(url)
  url = get_next_page(soup)
  if not url:
    break
  print(url)
  
# Create csv and write dict
# with open('extract.csv', 'w+') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(bookLink)
