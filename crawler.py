from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 設定瀏覽器選項
options = Options()
# 建立 driver
s = Service(r"chromedriver.exe")
chrome = webdriver.Chrome(service=s, options=options)
# 存取 Website
url = "https://stue1202.github.io/"
chrome.get(url)
time.sleep(3)
new_team=chrome.find_element(By.TAG_NAME,'input')
new_team.send_keys("week 9 homework")
time.sleep(2)

new_team.send_keys(Keys.ENTER)
time.sleep(2)

chrome.close()