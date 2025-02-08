from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
import json
import argparse

parser = argparse.ArgumentParser(prog='parkbot', description='Check the crystal mountain parking website for availability for a given day')
parser.add_argument('--day',type=int,required=True)
parser.add_argument('--month',type=int,required=True)
parser.add_argument('--year', type=int,default=2025)
args = parser.parse_args()

options = Options()
options.add_argument('--headless=new')
cService = webdriver.ChromeService()
driver = webdriver.Chrome(service=cService, options=options)

driver.get('https://parking.crystalmountainresort.com')
# give it a sec for javascript to load
time.sleep(1)

cal_entries = driver.find_elements(By.CSS_SELECTOR, f'#calendar_{args.year}-{args.month:02d} .calendar_day')
cal_entries = [entry for entry in cal_entries if entry.text == str(args.day)]

if len(cal_entries) != 1:
    print(f"unexpected html. found {len(cal)} matching calendar entries, wanted 1")
    exit(1)
cal = cal_entries[0]
data = json.loads(cal.get_attribute('data-json'))
title = data['title']
if 'Car Parking' not in title:
    print("couldn't find correct html element")
    exit(1)
if 'SOLD OUT' in title:
    print(f"sold out for {args.month}/{args.day}/{args.year}")
    exit(1)

print("PARKING AVAILABLE!!!")
