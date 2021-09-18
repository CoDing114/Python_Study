import requests
from bs4 import BeautifulSoup
import re

for year in range(2018, 2022):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84".format(
        year)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    # 네이버 영화 순위 가져오기 [ 이지미 저장 ]
    items = soup.find_all("div", attrs={"class": "thumb"})
    # enumerate:인덱스 번호와 컬렉션의 원소를 tuple형태로 반환합니다.
    for idx, item in enumerate(items):
        images_url = item.find("img")["src"]

        # 파일 저장을 위해 url을 변수에 저장
        image_res = requests.get(images_url)
        image_res.raise_for_status()

        # movie{year}_{index}.jpg 으로 파일 저장하기
        with open("movie{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

            if idx >= 4:    # 상위 5개 이미지까지만 다운로드
                break   # 반복문 탈출
