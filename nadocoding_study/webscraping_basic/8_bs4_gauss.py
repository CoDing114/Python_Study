import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# # 만화 제목과 링크 가져오기
# cartoons = soup.find_all("td", attrs={"class", "title"})
# # title = cartoons[0].a.get_text()
# # link = cartoons[0].a["href"]
# # print(title)
# # print("https://comic.naver.com" + link)
# # 반복문 활용 하여 타이틀 + url 로 정리
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_retes = 0
kartoons = soup.find_all("div", attrs={"class", "rating_type"})
for kartoon in kartoons:
    rate = kartoon.find("strong").get_text()
    print(rate)
    total_retes += float(rate)
print("전체 점수:", total_retes)
print("평균 점수:", total_retes / len(kartoons))
