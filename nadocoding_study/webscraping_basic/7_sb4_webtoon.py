import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
# find_all: 조 건에 해당하는 모든 element를 가져온다
cartoons = soup.find_all("a", attrs={"class": "title"})
# clsss 속성이 title 인 모든 "a" element 를 반환
for cartoon in cartoons:
    print(cartoon.get_text())
