from categoryLink import scrapCategoryLink

# specify the url
url = 'http://books.toscrape.com/index.html'
categoryLink = scrapCategoryLink(url)

print(0, len(categoryLink))