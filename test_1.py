# import
from get_url_category import get_url_category
from get_book import get_book
from get_url_book import get_url_book
from save_csv import save_book_csv
from get_data import get_data

rows = []
url = 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html'
# specify the url
# url = 'http://books.toscrape.com/index.html'
# url_category = get_url_category(url)


def get_next_page(soup):
    page = soup.find('ul', attrs={'class': 'pager'})
    if page.find('li', attrs={'class': 'next'}):
        url = 'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/' + \
            str(page.find('li', attrs={'class': 'next'}).find('a')['href'])
        return url
    else:
        return


def get_all_page(url):
    url_book = get_url_book(url)
    return url_book


def get_all_book(url_book):
    for i in range(len(url_book)):
        book = get_book(url_book[i])
        # write each result to rows
        rows.append(book)


url_book = get_all_page(url)

while True:
    soup = get_data(url)
    url = get_next_page(soup)
    if not url:
        break
    else:
        print(url)
        url_book = get_all_page(url)


get_all_book(url_book)
print(rows)
# Create csv and write dict
save_book_csv(rows)
