from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://bank.shinhan.com/index.jsp#020501010200'

driver = webdriver.Safari()
driver.maximize_window()
driver.get(url)
driver.implicitly_wait(15)

sort = driver.find_element(By.XPATH, '//*[@id="rad_sort"]/div[2]/label')
driver.execute_script("arguments[0].click();", sort)

exrate = driver.find_element(By.XPATH, '//*[@id="grd_list_1_cell_0_5"]/nobr').text
exrate = float(exrate.replace(',',''))
driver.close()
