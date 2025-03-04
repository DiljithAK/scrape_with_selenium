import os
from bs4 import BeautifulSoup
import pandas as pd

def get_book_name(soup):
    try:
        book_h1 = soup.find('h1')
        book_name = book_h1.text
    except:
        book_name = ''
    return book_name

def get_price(soup):
    try:
        price = soup.find('p', attrs={'class': 'price_color'})
        price_text = price.text
        price_text = price_text.replace("£", "") # Remove £ from the extracted data
    except:
        price_text = ''
    return price_text

def get_description(soup):
    try:
        description_div = soup.find('div', attrs={'id': 'product_description'})
        description = description_div.find_next('p')
        des_text = description.text
    except:
        des_text = ''
    return des_text

def get_image(soup):
    try:
        book_image_div = soup.find('div', attrs={'class': 'thumbnail'})
        image_tag = book_image_div.find('img')
        image_link = f"https://books.toscrape.com/{image_tag['src']}"
    except:
        image_link = ''
    return image_link

def make_csv(data):
    # create DataFrame using dictionary
    df = pd.DataFrame.from_dict(data)
    os.makedirs('scrape_with_selenium_103/data/result', exist_ok=True)
    df.to_csv('scrape_with_selenium_103/data/result/products.csv', index=False)

# To make the code inside the if run only when the file being runned
if __name__ == '__main__':

    # Create dictionary to store extracted data
    data = {'book': [], 'price': [], 'decription': [], 'image': []}

    # Get all the files in the product directory
    for file in os.listdir('scrape_with_selenium_103/data/products'):

        # Loop through the html files in the product directory
        with open(f'scrape_with_selenium_103/data/products/{file}', 'r', encoding='utf-8') as f:

            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')

            # Extract the data from the soup and append the value in data
            data['book'].append(get_book_name(soup))
            data['price'].append(get_price(soup))
            data['decription'].append(get_description(soup))
            data['image'].append(get_image(soup))

            make_csv(data)

