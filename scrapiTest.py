# import
from get_url_category import get_url_category
from get_book import get_book
from get_url_book import get_url_book
from save_csv import save_book_csv

rows = []

# specify the url
url = 'http://books.toscrape.com/index.html'
url_category = get_url_category(url)

def get_all_page(url_category):
    for i in range(1, int(len(url_category))):
        for x in range(9):
            if x == 1:
                url_book = url_category[i] + 'index.html'
                url_book = get_url_book(url)
            else:
                url = url_category[i] + '/page-' + \
                str(i) + '.html'
                url_book = get_url_book(url)
    return url_book


url_book = get_all_page(url_category)


def get_all_book(url_book):
    for i in range(len(url_book)):
        book = get_book(url_book[i])
        # write each result to rows
        rows.append(book)

get_all_book(url_book)

# Create csv and write dict
save_book_csv(rows)