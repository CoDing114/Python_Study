import requests
from bs4 import BeautifulSoup
import re

for i in range(0, 6):
    print("페이지:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(
        i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    # 쿠팡 노트북 가격 정보 가져오기
    items = soup.find_all(
        "li", attrs={"class": re.compile("^search-product")})  # dl태그 - class 가 ^search-product-wrap으로 시작하는 element 전부 찾기
    for item in items:
        # 광고 제품 제외
        ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
        if ad_badge:
            # print(" < 광고 상품 제외 합니다 > ")
            continue  # 내용 제되 됨

        names = item.find("div", attrs={"class": "name"}).get_text()    # 제품명

        # 삼성 제품 제외
        if "삼성" in names:
            # print("삼성 제품 제외 합니다")
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
        links = item.find("a", attrs={"class": "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) >= 50:
            # print("제품명:", names, "가격:", price,
            #       "평점:", rate, "평점 수:", rate_count)
            print(f"제품명 : {names}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count}개)")
            print("바로가기 :{}".format("https://www.coupang.com" + links))
            print("-"*100)  # 줄 긋기

"""
페이지: 0
제품명 : 레노버 2020 Gaming 3i 15IMH LEGEND PRO, 오닉스 블랙, 코어i5 10세대, 512GB, 16GB, WIN10 Home, 81Y400DGKR
가격 : 1,088,120    
평점 : 5.0점 (148개)
바로가기 :https://www.coupang.com/vp/products/1713335697?itemId=6062714749&vendorItemId=73359612226
----------------------------------------------------------------------------------------------------
제품명 : LG전자 2020 울트라 PC 14, 화이트, 셀러론, 512GB, 8GB, WIN10 Home, 14U390-ME1TK
가격 : 555,000
평점 : 4.5점 (244개)
바로가기 :https://www.coupang.com/vp/products/4841548763?itemId=6257652932&vendorItemId=73553348809
----------------------------------------------------------------------------------------------------
제품명 : 델 2020 Inspiron 15, 코어i7 10세대, 512GB, 16GB, WIN10 Pro, DN7501-WP06KR
가격 : 1,468,940
평점 : 5.0점 (54개)
바로가기 :https://www.coupang.com/vp/products/2343083054?itemId=6254502832&vendorItemId=73550216036
----------------------------------------------------------------------------------------------------
페이지: 1
제품명 : 레노버 2020 Gaming 3i 15IMH LEGEND PRO, 오닉스 블랙, 코어i5 10세대, 512GB, 16GB, WIN10 Home, 81Y400DGKR
가격 : 1,088,120
평점 : 5.0점 (148개)
바로가기 :https://www.coupang.com/vp/products/1713335697?itemId=6062714749&vendorItemId=73359612226
----------------------------------------------------------------------------------------------------
제품명 : 레노버 2021 ThinkPad E15, 블랙, 라이젠7 4세대, 512GB, 16GB, WIN10 Pro, 20YG0015KR
가격 : 1,106,530
평점 : 5.0점 (67개)
바로가기 :https://www.coupang.com/vp/products/5762131379?itemId=9761259195&vendorItemId=77044958094&pickType=COU_PICK
----------------------------------------------------------------------------------------------------
제품명 : LG전자 2020 울트라 PC 14, 화이트, 셀러론, 512GB, 8GB, WIN10 Home, 14U390-ME1TK
가격 : 555,000
평점 : 4.5점 (244개)
바로가기 :https://www.coupang.com/vp/products/4841548763?itemId=6257652932&vendorItemId=73553348809
----------------------------------------------------------------------------------------------------
"""
