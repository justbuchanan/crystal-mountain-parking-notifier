from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# TODO: refactor so that the date isn't hard-coded

import time
import json

options = Options()
options.add_argument('--headless=new')
cService = webdriver.ChromeService()
driver = webdriver.Chrome(service=cService, options=options)

driver.get('https://parking.crystalmountainresort.com')
# give it a sec for javascript to load
time.sleep(1)

cal = driver.find_elements(By.CSS_SELECTOR, '#calendar_2025-02 .calendar_day[data-date="2025-02-09T08:00:00.000Z"]')
if len(cal) != 1:
    print(f"unexpected html. found {len(cal)} entries, wanted 1")
    exit(1)
x = cal[0]
data = json.loads(x.get_attribute('data-json'))
title = data['title']
if 'Car Parking' not in title:
    print("couldn't find correct html element")
    exit(1)
if 'SOLD OUT' in title:
    print("sold out for 2/9")
    exit(1)

print("PARKING AVAILABLE!!!")
