import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

# 크롬 브라우저 설정
browser = webdriver.Chrome('D:\Downloads\coding\chromedriver.exe')    # "./chromedriver.exe"
browser.maximize_window()   # 창 최대화

# 네이버 항공권 이동
url = "https://beta-flight.naver.com/"
browser.get(url) 

# 가는 날 선택 클릭
# browser.find_element_by_link_text("가는 날").click()
# browser.find_elements_by_class_name("tabContent_option__2y4c6 select_Date__1aF7Y")
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button")))
# 이번달 27일, 다음달 28일 선택
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[1].click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/button").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[1]/button").click()

# 여행지 선택 (괌)
browser.find_element_by_class_name("Popular_button__3LeIb").click()

# 지정 시간 동안 로딩을 기다리되 로딩 되는 즉시 실행, 실패시 브라우저 종료
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/ul/li[1]")))
finally:
    print("정보 로딩 실패")
    browser.quit()

# 일정 정보 출력
elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/ul/li[1]")
print(elem.text) 
elem.click()

elem = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]")))

# 티켓 정보 출력
elem = browser.find_elements_by_class_name("result")[0]
print(elem.text) 