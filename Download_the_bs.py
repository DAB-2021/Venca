#Selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

companies = ["https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=174660",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=274834",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=214610",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=716078",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=864074",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=375274",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=620801",
"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId=712283"]

compare = ["výroční zpráva [2021]","výroční zpráva [2020]","výroční zpráva [2019]","výroční zpráva [2018]","výroční zpráva [2017]"]

for zprava in compare:
	pass
	for link in companies:
		driver.get(link)

		main = driver.find_element_by_class_name("list")
		tbody = main.find_element(By.TAG_NAME, "tbody")
		rows = tbody.find_elements(By.TAG_NAME, "tr")

		col = 0

		for row in rows:
			col = row.find_elements(By.TAG_NAME,"td")[1].text
			print(col)
			if zprava in col:
				cell = row.find_elements(By.TAG_NAME,"td")[0].text
				driver.find_element(By.PARTIAL_LINK_TEXT,cell).click()
				break
		try:
		   	element = WebDriverWait(driver, 2).until(
	        	EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "kB"))
	    	)
		   	driver.find_element(By.PARTIAL_LINK_TEXT,'kB').click()
		   	time.sleep(1)
		except:
		  	break		

driver.quit()