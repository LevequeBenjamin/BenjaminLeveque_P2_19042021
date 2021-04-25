# import function
from get_data import get_data
# import librairies
import urllib.request
from urllib.parse import urljoin


# find results
def get_book(url):
    # request get
    soup = get_data(url)
    article = soup.find('article', class_= 'product_page')
    table = article.find('table', class_= 'table')
    tds = table.find_all('td')
    # product_page_url
    product_page_url = url
    # universal_product_code(upc)
    upc = table.find('td').get_text()
    # title
    title = article.find('h1').get_text().replace('/', '_')
    # price_including_tax
    price_including_tax = tds[3].get_text()
    # price_excluding_tax
    price_excluding_tax = tds[2].get_text()
    # number_available
    number_available = tds[5].get_text().strip('In stock ()')
    # product_description
    product_description = article.find_all('p')[3].get_text()
    # categorie
    category = soup.find('ul', class_= 'breadcrumb').find_all('li')[2].get_text().strip('\n')
    # review_rating
    reviews_rating = soup.find('p', class_= 'star-rating')['class'][1].lower() 
    # imageUrl
    image_source = article.find(
        'div', class_= 'item').find('img')['src']
    image_url = urljoin('http://books.toscrape.com/', image_source)
    # downloads image
    image_file = title.replace(" ", "_").lower()
    filename = image_file + '.jpg'
    urllib.request.urlretrieve(image_url, 'downloads/images/' + filename)

    return(product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, reviews_rating, image_url, filename)
