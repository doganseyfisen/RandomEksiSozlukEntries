from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Firefox()
url = "https://eksisozluk1923.com/rammstein--32863?p="
page_counter = 1
entries = []

while page_counter <= 5:
    random_page = random.randint(1, 227)
    new_url = url + str(random_page)
    browser.get(new_url)
    elements = browser.find_elements(By.CSS_SELECTOR, '.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(1)
    page_counter += 1

for entry in entries:
    print("=========")
    print(entry)

browser.close()


