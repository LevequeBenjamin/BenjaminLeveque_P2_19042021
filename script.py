# import librairies
from bs4 import BeautifulSoup
from tqdm.auto import tqdm
from time import sleep

# import modules_p2
from modules_p2.get_url_category import get_url_category
from modules_p2.get_book import get_book
from modules_p2.get_url_book import get_url_book
from modules_p2.save_csv_book import save_csv_book
from modules_p2.get_data import get_data


# specify the url
url_index = 'https://books.toscrape.com/index.html'

# get category url
def get_url(url_index: str) -> list:
    """[Find all urls for each category of books]

    Args:
        url_index (str): [url of the main book.toscrap page]

    Returns:
        list: [a list with the urls of each category]
    """
    url = get_url_category(url_index)
    return url


# get next page url
def get_next_page(soup: BeautifulSoup, url: str) -> str:
    """[find the next page of a book category if there is one]

    Args:
        soup (BeautifulSoup): [A data structure representing a parsed HTML or XML document]
        url (str): [url of a book category]

    Returns:
        str: [The next page of a book category if there is one]
    """
    url = url.replace(url.split('/')[-1], '')
    if soup.find('ul', class_='pager'):
        page = soup.find('ul', class_='pager')
        if page.find('li', class_='next'):
            url = url + \
                str(page.find('li', class_='next').find('a')['href'])
            return url
        else:
            return
    else:
        return


# get page url
def get_all_page(url: str) -> list:
    """[Find all urls of books in a category]

    Args:
        url (str): [url of a book category]

    Returns:
        list: [A list of book urls]
    """
    url_book = get_url_book(url)
    return url_book


# get book
def get_all_book(url_book: list, rows: list):
    """[From a list of book urls, it finds all the information and adds them to rows]

    Args:
        url_book (list): [A list of book urls]
        rows (list) : [A list of data:
        product_page_url,
        upc,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        reviews_rating,
        image_url,
        filename]
    """
    # loop from book url
    for i in range(len(url_book)):
        book = get_book(url_book[i])
        # write each result to rows
        rows.append(book)


# get book url
def srap_books(url: str, rows: list):
    """[From a book category url, call url_book (), get_all_book () and get_next_page ()]

    Args:
        url (str): [url of a book category]
        rows (list) : [A list of data:
        product_page_url,
        upc,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        reviews_rating,
        image_url,
        filename]
    """
    url_book = get_all_page(url)
    get_all_book(url_book, rows)
    # loop to get the next pages
    while True:
        soup = get_data(url)
        url = get_next_page(soup, url)
        if not url:
            break
        else:
            url_book = get_all_page(url)
            get_all_book(url_book, rows)
    del url_book[:]


url = get_url(url_index)


if __name__ == '__main__':
    # loop from second category url
    for i in tqdm(range(1, len(url))):
        rows = []
        srap_books(url[i], rows)
        # create csv and write rows list
        save_csv_book(rows)
        # progress bar
        sleep(0.01)
        # cancel list
        del rows[:]
