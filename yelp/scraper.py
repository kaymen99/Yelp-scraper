from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time, os
from selenium.webdriver.chrome.options import Options 
import pandas as pd
from parsel import Selector


def scrape(s_business, s_location, s_num_page):
	opts = Options()
	opts.add_argument("user-agent=Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36")
	opts.add_argument('--headless')
	opts.add_argument('window-size=1920x1080')
	driver = webdriver.Chrome(options=opts)

	driver.get('https://www.yelp.com')
	time.sleep(8)

	print('Searching')
	buissness = '//*[@id="find_desc"]'
	buissness_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, buissness)))
	buissness_element.click()
	buissness_element.send_keys(s_business)


	location = '//*[@id="dropperText_Mast"]'
	location_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location)))
	location_element.click()
	location_element.send_keys(s_location)

	search = '//*[@id="header-search-submit"]'
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search))).click()
	time.sleep(8)



	next_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.next-link')))

	links = []
	links.append([link.find_element_by_tag_name('a').get_attribute('href') for link in driver.find_elements_by_class_name('css-1l5lt1i')])

	for i in range(s_num_page - 1):
	    next_page.click()
	    time.sleep(5)
	    liste = [link.find_element_by_tag_name('a').get_attribute('href') for link in driver.find_elements_by_class_name('css-1l5lt1i')]
	    links.append(liste)
	    next_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.next-link')))

    

	print('Start collecting data')

	
	elements = []
	i = 0
	for page in links:
		for url in page:
			driver.get(url)
			time.sleep(5)
			sel = Selector(driver.page_source)
			name = sel.css('.css-11q1g5y::text').get()
			link = driver.current_url
			website = sel.css('.css-aml4xx+ .css-1h1j0y3 .css-ac8spe::text').get()
			phone = sel.css('.css-aml4xx+ .css-1h1j0y3::text').get()
			address = sel.css('.vertical-align-middle__373c0__eJLXr .css-chtywg::text').get()
			work_hours = sel.css('.margin-l1__373c0__Z_Kgf .css-bq71j2::text').get()
			types = '|'.join(sel.css('.css-166la90::text').getall()[:3])
			reviews_number = sel.css('.arrange-unit-fill__373c0__3cIO5.nowrap__373c0__AzEKB .css-bq71j2::text').get()
			rating = sel.css('.overflow--hidden__373c0__1TJqF::attr(aria-label)').get()
			elements.append([name, website, phone, address, work_hours, types, reviews_number, rating, link])
		print(f'finished page {i + 1}')
		i += 1
	 

	data = pd.DataFrame(elements, columns=['name', 'website', 'phone', 'address', 'work_hours', 'types', 'reviews_number', 'rating', 'link'])
	save_path = os.path.join(os.getcwd(), 'data.csv')
	data.to_csv(save_path)

	print('finished')
	driver.quit()






