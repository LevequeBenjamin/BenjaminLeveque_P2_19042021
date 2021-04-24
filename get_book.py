# import function
from get_data import get_data


# find results
def get_book(url):
    # request get
    soup = get_data(url)
    article = soup.find('article', attrs={'class': 'product_page'})
    table = article.find('table', attrs={'class': 'table'})
    tds = table.findAll('td')
    # universal_product_code(upc)
    upc = table.find('td').getText()
    # title
    title = article.find('h1').getText()
    # price_including_tax
    price_incl_tax = tds[3].getText()
    # price_excluding_tax
    price_excl_tax = tds[2].getText()
    # number_available
    number_available = tds[5].getText().strip('In stock ()')
    # product_description
    p = article.findAll('p')
    product_description = p[3].getText()
    # categorie
    li = soup.find('ul', attrs={'class': 'breadcrumb'}).findAll('li')
    category = li[2].getText().strip('\n')
    # review_rating
    number_reviews = soup.find('p', attrs={'class': 'star-rating'})['class'][1].lower() 
    # imageUrl
    image_source = article.find(
        'div', attrs={'class': 'item'}).find('img')['src']
    image_url = 'http://books.toscrape.com/' + image_source.strip('../..')

    return(url, upc, title, price_incl_tax, price_excl_tax, number_available, product_description, category, number_reviews, image_url)
