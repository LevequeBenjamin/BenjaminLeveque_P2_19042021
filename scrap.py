# import
from get_url_category import get_url_category
from get_book import get_book
from get_url_book import get_url_book
from save_csv import save_book_csv

rows = []

# specify the url
url = 'http://books.toscrape.com/index.html'
url_category = get_url_category(url)

def get_all_page():
    for i in range(9):
        if i == 1:
            url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
            url_book = get_url_book(url)
        else:
            url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + \
            str(i) + '.html'
            url_book = get_url_book(url)
    return url_book

url_book = get_all_page()

def get_all_book(url_book):
    for i in range(len(url_book)):
        book = get_book(url_book[i])
        # write each result to rows
        rows.append(book)

get_all_book(url_book)
print(rows)
# Create csv and write dict
save_book_csv(rows)


