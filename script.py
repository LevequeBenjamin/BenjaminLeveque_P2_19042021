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
    # loop from second category url
    for i in range(1, len(url)):       
        # get next page url
        def get_next_page(soup, url):
            url = url.replace(url.split('/')[-1], '')
            if soup.find('ul', class_= 'pager'):
                page = soup.find('ul', class_= 'pager')
                if page.find('li', class_= 'next'):
                    url = url + \
                        str(page.find('li', class_= 'next').find('a')['href'])
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
            # loop from book url
            for i in range(len(url_book)):
                book = get_book(url_book[i])
                # write each result to rows
                rows.append(book)

        # get book url
        def srap_books(url):
            url_book = get_all_page(url)
            get_all_book(url_book)
            # loop to get the next pages
            while True:
                soup = get_data(url)
                url = get_next_page(soup, url)
                if not url:
                    break
                else:
                    url_book = get_all_page(url)
                    get_all_book(url_book)
            del url_book[:]

        #url_book = 
        srap_books(url[i])
        # create csv and write rows list
        save_book_csv(rows)
        # cancel list
        del rows[:]


url = get_url(url_index)
get_all_scrap(url)
