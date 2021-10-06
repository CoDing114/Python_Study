import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# headless 사용중 주의할점:
# 웹크롤링 중 headless 사요시 user agent값이 HeadlessChrome으로 요청하는걸 볼수잇다
# headless 사요시엔 user agent를 필요시 수정.
# Chrome:    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36
# headless:  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/94.0.4606.71 Safari/537.36

# headless를 활용하면 브라우저 창 안켜진 상태로 진행가능하다
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
# options.add_argument('lang=zh_CN.UTF-8')  # 크롬 브라우저 언어 설정

browser = webdriver.Chrome("D:\Downloads\coding\chromedriver.exe",options=options)

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()