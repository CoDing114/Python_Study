import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
# headless를 활용하면 브라우저 창 안켜진 상태로 진행가능하다
options = webdriver.ChromeOptions() # 进入浏览器设置
# options.headless = True # headless를 활용하면 브라우저 창 안켜진 상태로 진행가능하다
options.add_argument("window-size=1920x1080")   # 실행할 창 크기 설정
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36")
# options.add_argument('lang=zh_CN.UTF-8')  # 크롬 브라우저 언어 설정

# 화면 스크롤(#1)
# def drop_down():
#     '''执行页面滚动操作'''  # javascript
#     for x in range(1, 30, 4):  # 在你不断地下拉过程中,页面高度会变
#         time.sleep(1)
#         j = x / 9
#         # document.documentElement.scrollTop 指定滚动条的位置
#         # document.documentElement.scrollHeight 获取浏览器页面的最大高度
#         js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
#         browser.execute_script(js)


browser = webdriver.Chrome("D:\Downloads\coding\chromedriver.exe",options=options)


# 페이지 이동
url = "https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl9lYm9va190b3BzZWxsaW5nEEQYASIECAUILA%3D%3D:S:ANO1ljLtPtQ&gsr=CiuyAigKIAoacHJvbW90aW9uX2Vib29rX3RvcHNlbGxpbmcQRBgBIgQIBQgs:S:ANO1ljJFgfM"
browser.get(url)
time.sleep(3)
# drop_down()   #화면 스크롤(#1)

print("스크롤 완료")
browser.get_screenshot_as_file("google_books.png")  # 잘 작동하는지 스크린샷을 남겨보자


soup = BeautifulSoup(browser.page_source,"lxml")

movies = soup.find_all("div",attrs={"class":["Vpfmgd"]})
# print(len(movies))
# print(movies)

# 화면 스크롤(#2)
interval = 2    # 2초에 한번씩 스크롤 내림

# # 지정 위치로 스크롤 내리기
# # 모니터(해상도) 높이인 2160 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)")   # 1920 x 1080
# browser.execute_script("window.scrollTo(0,2160)")   # 3840 x 2160

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height=curr_height

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
