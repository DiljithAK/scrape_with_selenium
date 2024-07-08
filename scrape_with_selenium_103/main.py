import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from fake_useragent import UserAgent

def setup_driver(path):
    service = Service(path)
    options = webdriver.ChromeOptions()
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def save_book_html(driver, page_no, book_no):
    try:
        page_content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'content'))
        )
        html = page_content.get_attribute("outerHTML")
        os.makedirs("scrape_with_selenium_103/products", exist_ok=True)
        with open(f"scrape_with_selenium_103/products/book_{page_no}_{book_no}.html", "w", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(f"Error saving HTML for book {book_no}: {e}")

def main():
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    for page_no in range(1, 11):
        if page_no % 3 == 1:
            if page_no > 1:
                driver.quit()
                time.sleep(5)
            driver = setup_driver(PATH)
        
        URL = f"https://books.toscrape.com/catalogue/page-{page_no}.html"
        driver.get(URL)

        try:
            books = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'product_pod'))
            )

            for book_no, book in enumerate(books):
                book_link = book.find_element(By.TAG_NAME, 'a')
                link = book_link.get_attribute('href')

                time.sleep(random.uniform(2, 3))

                driver.get(link)

                save_book_html(driver, page_no, book_no)

                driver.back()
        except Exception as e:
            print(f"An error occurred: {e}")
    driver.quit()

if __name__ == '__main__':
    main()
