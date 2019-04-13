import time
import json 
from selenium import webdriver
import sys
import redis	

r = redis.Redis(host='153.92.5.10', port=6379, db=0)
count = 1

with open('data.json', 'r') as json_file:
	data = json.loads(json_file.read())
	path = '/screenshots'
	for row in data:
		url = row['link_page']
		if not r.exists('webpage:' + str(count)):
			chrome_options = webdriver.ChromeOptions()
			chrome_options.add_argument('--headless')
			chrome_options.add_argument('--no-sandbox')
			chrome_options.add_argument('--disable-dev-shm-usage')
			chrome_options.add_argument("--start-maximized")
			DRIVER = 'chromedriver'
			driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)
			browser = driver
			browser.set_window_size(1366, 768)
			browser.get(url)
			browser.implicitly_wait(7.5) # seconds
			total_height = browser.execute_script("return document.body.parentNode.scrollHeight")
			browser.quit()

			# 2. get screenshot
			browser = webdriver.Chrome(chrome_options=chrome_options)
			browser.set_window_size(1386, total_height)
			browser.get(url)
			browser.implicitly_wait(7.5) # seconds
			browser.save_screenshot(path + '/' + str(count) + '.png')
			browser.quit()
			r.set('webpage:' + str(count), 1)
			print(str(count))
		count = count + 1
