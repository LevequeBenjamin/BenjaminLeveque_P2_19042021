# import function
from get_url_category import get_url_category
from get_book import get_book
from get_url_book import get_url_book
from save_csv import save_book_csv
from get_data import get_data

rows = []
url = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'


def get_next_page(soup, url):
    url = url.replace(url.split('/')[-1], '')  
    if soup.find('ul', attrs={'class': 'pager'}):
        page = soup.find('ul', attrs={'class': 'pager'})
        if page.find('li', attrs={'class': 'next'}):
            url = url + \
                str(page.find('li', attrs={'class': 'next'}).find('a')['href'])
            return url
        else:
            return
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


def srap_books(url):
    url_book = get_all_page(url)
    while True:
        soup = get_data(url)
        url = get_next_page(soup, url)
        if not url:
            break
        else:
            url_book = get_all_page(url)
    return url_book
    

url_book = srap_books(url)
get_all_book(url_book)


print(rows)
save_book_csv(rows)
