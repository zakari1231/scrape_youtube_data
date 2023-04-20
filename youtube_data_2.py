from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_driver():
    firefox_options = Options()
    # firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe", options=firefox_options)
    driver.implicitly_wait(9)
    return driver

driver = get_driver()

driver.get('https://www.youtube.com/')
search = driver.find_element(By.XPATH, '//input[@id="search"]')
search.send_keys("python")
# search.send_keys(Keys.ENTER) #using the enter key 
# searchbutton = driver.find_element(By.XPATH,'//*[@id="search-icon-legacy"]') 
# searchbutton.click() # using the click method()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-icon-legacy"]'))).click()
# driver.implicitly_wait(10)
# print(driver.title)