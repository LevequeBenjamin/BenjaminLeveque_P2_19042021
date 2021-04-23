# import function
from get_url_category import get_url_category
from get_book import get_book
from get_url_book import get_url_book
from save_csv import save_book_csv
from get_data import get_data


# specify the url
url_index = 'https://books.toscrape.com/index.html'

# get category url
def get_url(url_index):
    url = get_url_category(url_index)
    return url

# get all book
def get_all_scrap(url):
    rows = []
    for i in range(1, len(url)):
        del rows[:]
        # get next page url
        def get_next_page(soup, url):
            url = url.replace(url.split('/')[-1], '')
            if soup.find('ul', attrs={'class': 'pager'}):
                page = soup.find('ul', attrs={'class': 'pager'})
                if page.find('li', attrs={'class': 'next'}):
                    url = url + \
                        str(page.find('li', attrs={
                            'class': 'next'}).find('a')['href'])
                    return url
                else:
                    return
            else:
                return

        # get page url
        def get_all_page(url):
            url_book = get_url_book(url)
            return url_book
        
        # get book 
        def get_all_book(url_book):
            for i in range(len(url_book)):
                book = get_book(url_book[i])
                # write each result to rows
                rows.append(book)

        # get book url
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

        url_book = srap_books(url[i])
        get_all_book(url_book)
        # create csv and write dict
        save_book_csv(rows)
        del url_book[:]


url = get_url(url_index)
get_all_scrap(url)
