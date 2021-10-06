import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 화면 스크롤(#1)
def drop_down():
    '''执行页面滚动操作'''  # javascript
    for x in range(1, 30, 4):  # 在你不断地下拉过程中,页面高度会变
        time.sleep(1)
        j = x / 9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        browser.execute_script(js)


browser = webdriver.Chrome('D:\Downloads\coding\chromedriver.exe')
#브라우저 최대화
# browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl9lYm9va190b3BzZWxsaW5nEEQYASIECAUILA%3D%3D:S:ANO1ljLtPtQ&gsr=CiuyAigKIAoacHJvbW90aW9uX2Vib29rX3RvcHNlbGxpbmcQRBgBIgQIBQgs:S:ANO1ljJFgfM"
browser.get(url)
time.sleep(3)
drop_down()   #화면 스크롤(#1)

# # 화면 스크롤(#2)
# interval = 2    # 2초에 한번씩 스크롤 내림

# # # 지정 위치로 스크롤 내리기
# # # 모니터(해상도) 높이인 2160 위치로 스크롤 내리기
# # browser.execute_script("window.scrollTo(0,1080)")   # 1920 x 1080
# # browser.execute_script("window.scrollTo(0,2160)")   # 3840 x 2160

# # 현재 문서 높이를 가져와서 저장
# prev_height = browser.execute_script("return document.body.scrollHeight")

# # 반복 수행
# while True:
#     #스크롤을 가장 아래로 내림
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#     # 페이지 로딩 대기
#     time.sleep(interval)

#     # 현재 문서 높이를 가져와서 저장
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     if curr_height == prev_height:
#         break
#     prev_height=curr_height


print("스크롤 완료")



soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div",attrs={"class":["Vpfmgd"]})
# print(len(movies))
# print(movies)

# 타이틀 가져오기
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

    # 할인 전 가격
    original_price = movie.find("span",attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title,"<할인되지 않은 영화 제외>")
        continue

    # 할인 후 가격
    price = movie.find("span",attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a",attrs={"class":"JC71ub"})["href"]
    # 올바른 링크: https://play.google.com/ + link

    print(f"제목:{title}")
    print(f"할인 전 금액:{original_price}")
    print(f"할인 후 금액:{price}")
    print("링크:","https://play.google.com" + link)
    print("-" *120)
