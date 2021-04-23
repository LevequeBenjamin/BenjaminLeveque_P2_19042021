# import libraries
from get_data import get_data
category_url = []


# find category url
def get_url_category(url):
    # request get
    soup = get_data(url)
    lis = soup.find('ul', attrs={'class': 'nav-list'}).findAll('li')
    # loop over results
    for li in lis:
        category_link = li.find('a')['href']
        category_link = 'http://books.toscrape.com/' + \
            category_link
        category_url.append(category_link)
    return category_url
