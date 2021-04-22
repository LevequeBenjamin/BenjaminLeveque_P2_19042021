# import
from get_data import get_data
book_url = []

# function get_url_book
def get_url_book(url):
    # request get
    soup = get_data(url)
    articles = soup.findAll('article', attrs={'class': 'product_pod'})

    for article in articles:
        link = article.find('a')['href']
        link = 'http://books.toscrape.com/catalogue/' + \
            link.strip('../../..')
        book_url.append(link)
    return book_url
