import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    URL = 'https://www.bikewale.com/'

    service = Service(PATH)
    driver = webdriver.Chrome(service = service)
    driver.get(URL)

    search_box_div = driver.find_element(By.CLASS_NAME, 'o-bfyaNx')
    input_fields = search_box_div.find_element(By.TAG_NAME, 'input')
    
    input_fields.send_keys('Honda Bikes')
    time.sleep(2)
    input_fields.send_keys(Keys.RETURN)

    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(1)

    bike_names = driver.find_elements(By.TAG_NAME, 'h3')

    second_page_links = []
    for index, bike_name in enumerate(bike_names):
        parent_a_tag = bike_name.find_element(By.XPATH, './ancestor::a[1]')
        
        # Get the href attribute of the parent <a> tag
        href = parent_a_tag.get_attribute('href')
        second_page_links.append(href)
        if index == 3:
            break

    if len(second_page_links) > 0:
        for index, page_link in enumerate(second_page_links):
            driver.get(page_link)
            time.sleep(1)
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(5)
            print(driver.title)
            driver.back()
            if index == 3:
                break
            time.sleep(2)

    time.sleep(5)
    driver.quit()
