import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all(
    "dl", attrs={"class": re.compile("^search-product-wrap")})  # dl태그 - class 가 ^search-product-wrap으로 시작하는 element 전부 찾기
# print(items[0].find("div", attrs={"class": "name"}).get_text())
for item in items:

    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print(" < 광고 상품 제외 합니다 > ")
        continue  # 내용 제되 됨

    names = item.find("div", attrs={"class": "name"}).get_text()    # 제품명

    # 삼성 제품 제외
    if "삼성" in names:
        print("삼성 제품 제외 합니다")
        continue
    price = item.find(
        "strong", attrs={"class": "price-value"}).get_text()    # 가격
    rate = item.find("em", attrs={"class": "rating"})    # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없는 제품 제외 합니다"
        continue
    rate_count = item.find(
        "span", attrs={"class": "rating-total-count"})   # 평점 수
    if rate_count:
        rate_count = rate_count.get_text()
        rate_count = rate_count[1:-1]
    else:
        rate_count = "평점 수 없는 제품 제외 합니다"
        continue

    # 평점 4.5 이상 평점수 50개 이상 상품만 보기
    if float(rate) >= 4.5 and int(rate_count) >= 50:
        print("제품명:", names, "가격:", price, "평점:", rate, "평점 수:", rate_count)
