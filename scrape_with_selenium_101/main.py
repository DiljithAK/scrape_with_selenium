import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

PATH = "C:\Program Files (x86)\chromedriver.exe"
URL = 'https://www.bikewale.com/'

service = Service(PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL)

page_title = driver.title

search_box_div = driver.find_element(By.CLASS_NAME, 'o-bfyaNx')
input_fields = search_box_div.find_element(By.TAG_NAME, 'input')

input_fields.send_keys('Honda Bikes')
time.sleep(1)
input_fields.send_keys(Keys.RETURN)

bike_names = driver.find_elements(By.TAG_NAME, 'h3')

with open('selenium_tutorial_1/bike_headings.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Bike Names'])
    for bike_name in bike_names:
        writer.writerow([bike_name.text])

time.sleep(5)
driver.quit()
