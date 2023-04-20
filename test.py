from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd

import json

option = Options()
option.headless = False

driver = webdriver.Firefox(executable_path=r"C:\Program Files\Mozilla Firefox\geckodriver.exe", options=option)
driver.implicitly_wait(5)
baseUrl = "https://youtube.com/"
keyword = "cs50"

def getChannelUrl():
    driver.get(f"{baseUrl}/search?q={keyword}")
    time.sleep(3)
    # allChannelList= driver.find_elements_by_css_selector("#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string")
    allChannelList = driver.find_elements(By.CSS_SELECTOR,"#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string")
    # links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),allChannelList)))
    # .find_element(By.LINK_TEXT, 'Continue')
    links = list(dict.fromkeys(map(lambda a: a.get_attribute('href'),allChannelList)))
    # print(allChannelList)
    # links = []
    # for link in allChannelList:
    #     the_link  = link.get_attribute('href')
    #     links.append(the_link)
    return links

def getChannelDetails(urls):
    details = []
    for url in urls:
        driver.get(f"{url}/about")
        # cname = driver.find_element_by_css_selector("#text.style-scope.ytd-channel-name").text
        # cname = driver.find_element(By.CSS_SELECTOR,"ytd-channel-name.ytd-c4-tabbed-header-renderer > div:nth-child(1) > div:nth-child(1) > yt-formatted-string:nth-child(1)")
        # cDess = driver.find_element_by_css_selector("#description-container > yt-formatted-string:nth-child(2)").text
        cDess = driver.find_element(By.CSS_SELECTOR,"#description-container > yt-formatted-string:nth-child(2)").text
        clink = url
        # otherLinkObj = driver.find_elements_by_css_selector("#link-list-container.style-scope.ytd-channel-about-metadata-renderer a.yt-simple-endpoint.style-scope.ytd-channel-about-metadata-renderer")
        otherLinkObj = driver.find_elements(By.CSS_SELECTOR,"#link-list-container.style-scope.ytd-channel-about-metadata-renderer a.yt-simple-endpoint.style-scope.ytd-channel-about-metadata-renderer")

        otherLinks = list(dict.fromkeys(map(lambda a: a.get_attribute("href"),otherLinkObj)))
        
        obj = {
            # "cname" : cname,
            "curl"  : clink,
            "cdesc" : cDess,
            "otherLinks" : otherLinks
        }
        details.append(obj)
    return details
if __name__ == "__main__":
    allChannelUrls = getChannelUrl()
    allChannelDetails = getChannelDetails(allChannelUrls)
    # print(allChannelDetails)
    df1 = pd.DataFrame(allChannelUrls)
    df1.to_csv('allChannelUrls.csv', index=False)
    df2 = pd.DataFrame(allChannelDetails)
    df2.to_csv('allChannelDetails.csv', index=False)


    