from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# option = Options
# option.headless = False

path = "C:\Program Files\Mozilla Firefox\geckodriver.exe"

driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe")
driver.get('https://www.youtube.com/')
# driver.implicitly_wait(5) 
# driver.switch_to.frame(0)
print(driver.title)

# search = driver.find_element(By.ID, "search") # using the By
search = driver.find_element(By.XPATH, '//input[@id="search"]') # using Xpath
# search = driver.find_element(By.CSS_SELECTOR, 'input.ytd-searchbox')# using css selector
# search = driver.find_element('id','search')

# search.send_keys("test")

# searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]') 
# searchbutton.click()
search.send_keys("python")
# search.send_keys(Keys.ENTER) #using the enter key 
# searchbutton = driver.find_element(By.XPATH,'//*[@id="search-icon-legacy"]') 
# searchbutton.click() # using the click method()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-icon-legacy"]'))).click()
driver.implicitly_wait(10)

# print(driver.title)

# # driver.quit()
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, 'ytd-item-section-renderer.style-scope:nth-child(2) > div:nth-child(3)'))
#     )
# finally:
all_videos = driver.find_elements(By.CSS_SELECTOR, 'ytd-playlist-renderer.style-scope:nth-child(1)')

print(len(all_videos))