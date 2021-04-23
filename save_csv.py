# import libraries
import csv

# Create csv and write rows to output file
def save_book_csv(rows):
    # extract category from the name
    with open(f'{rows[0][7].replace(" ", "_").lower()}.csv', 'w', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        # create and write headers to a list
        csv_writer.writerow(["product_page_url", "universal_product_code(upc)", "title", "price_including_tax",
                             "price_excluding_tax", "number_available", "product_description", "categorie", "review_rating", "image_url"])
        csv_writer.writerows(rows)
