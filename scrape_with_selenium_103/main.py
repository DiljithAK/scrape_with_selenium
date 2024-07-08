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
    options = webdriver.ChromeOptions() # Create chrome options instance
    ua = UserAgent()
    user_agent = ua.random # Get random user agent
    options.add_argument(f'user-agent={user_agent}') # Add uesr agent using chrome option instance
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def save_book_html(driver, page_no, book_no):
    try:
        # Wait element with class content to load
        page_content = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'content'))
        )
        
        # Get html code of the element
        html = page_content.get_attribute("outerHTML")
        os.makedirs("scrape_with_selenium_103/data/products", exist_ok=True) # Create directory if not exist
        # Write the html content into a html file
        with open(f"scrape_with_selenium_103/data/products/book_{page_no}_{book_no}.html", "w", encoding="utf-8") as f:
            f.write(html)
    except Exception as e:
        print(f"Error saving HTML for book {book_no}: {e}")

def main():
    PATH = "C:\Program Files (x86)\chromedriver.exe"

    for page_no in range(1, 11):
        # Quit and rebuild the driver after some pages
        if page_no % 3 == 1:
            if page_no > 1:
                driver.quit()
                time.sleep(5)
            driver = setup_driver(PATH)
        
        URL = f"https://books.toscrape.com/catalogue/page-{page_no}.html"
        driver.get(URL)

        try:
            # Wait till element with class product_pod to load
            books = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'product_pod'))
            )

            for book_no, book in enumerate(books[:6]):
                book_link = book.find_element(By.TAG_NAME, 'a')
                link = book_link.get_attribute('href') # Get detail page link

                time.sleep(random.uniform(2, 3)) # sleep for sometime to not over load the server

                driver.get(link) # Get detail page

                save_book_html(driver, page_no, book_no) # Get the html content

                driver.back() # Navigate back to book list from the detail page
        except Exception as e:
            print(f"An error occurred: {e}")
    driver.quit() # Quit the driver

if __name__ == '__main__':
    main() # Call main function
