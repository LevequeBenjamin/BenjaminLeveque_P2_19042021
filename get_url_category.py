# import
from get_data import get_data
category_url = []


# function get_url_category
def get_url_category(url):
    soup = get_data(url)
    lis = soup.find('ul', attrs={'class': 'nav-list'}).findAll('li')
    for li in lis:
        category_link = li.find('a')['href']
        category_link = 'http://books.toscrape.com/' + \
            category_link.strip('/index.html')
        category_url.append(category_link)
    return category_url
