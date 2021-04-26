# import function
from get_data import get_data


# find category url
def get_url_category(url: str) -> list:
    category_url = []
    # request get
    soup = get_data(url)
    lis = soup.find('ul', class_='nav-list').find_all('li')
    # loop over results
    for li in lis:
        category_link = li.find('a')['href']
        category_link = 'http://books.toscrape.com/' + \
            category_link
        category_url.append(category_link)
    return category_url
