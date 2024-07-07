import os
from bs4 import BeautifulSoup

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

if __name__ == '__main__':
    data = {'book': [], 'price': [], 'decription': [], 'image': []}
    for file in os.listdir('book_to_scrape/products'):
        with open(f'book_to_scrape/products/{file}', 'r', encoding='utf-8') as f:
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')

            data['book'].append(get_book_name(soup))
            data['price'].append(get_price(soup))
            data['decription'].append(get_description(soup))
            data['image'].append(get_image(soup))

    print(data)
