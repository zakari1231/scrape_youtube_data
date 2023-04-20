import time

from selenium import webdriver
from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# options = Options()
firefox_options = Options()
firefox_options.add_argument("--headless")
# firefox_options.add_argument("start-maximized")
# firefox_options.add_argument('--disable-notifications')

webdriver_service = 'C:\Program Files\Mozilla Firefox\geckodriver.exe'
driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe", options=firefox_options)
# driver = webdriver.Firefox(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 10)

url = "https://www.youtube.com/"
driver.get(url)

search = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]')))
search.click()
time.sleep(0.2)
search.send_keys("python")
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search-icon-legacy"]'))).click()

time.sleep(2)
print(driver.title)
time.sleep(2)
# all_videos = driver.find_elements(By.CSS_SELECTOR, 'ytd-playlist-renderer.style-scope:nth-child(1)')
# all_videos = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-item-section-renderer').text
all_videos = driver.find_element(By.XPATH, '//*[@id="contents"]').get_attribute('innerHTML')
print(all_videos)

