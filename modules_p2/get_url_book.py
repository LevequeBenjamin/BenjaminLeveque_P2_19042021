# import modules_p2
from modules_p2.get_data import get_data


# find book url
def get_url_book(url: str) -> list:
    """[Find all book urls on a page]

    Args:
        url (str): [url of a book category page]

    Returns:
        list: [Returns a list with all the urls of the books on a page]
    """
    book_url = []
    # request get
    soup = get_data(url)
    articles = soup.find_all('article', class_='product_pod')
    for article in articles:
        link = article.find('a')['href']
        # remove unwanted characters
        link = 'http://books.toscrape.com/catalogue/' + \
            link.strip('../../..')
        book_url.append(link)
    return book_url
