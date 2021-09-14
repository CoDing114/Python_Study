import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# 뷰티플숲 상세정보
# 구글링: BeautifulSoup
# 추천 사이트: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)  # 타이틀 출력
# print(soup.title.get_text())    # 타이틀 텍스트만 출력
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs)  # a element 의 속성 정보를 출력
# print(soup.a["href"]) # a element 의 href 속성 '값' 정보 출력

# class="_bigImgLink"인 "a" element 를 찾아줘
# print(soup.find("a", attrs={"class": "_bigImgLink"}))
# class="_bigImgLink"인 element 를 찾아줘
# print(soup.find(attrs={"class": "_bigImgLink"}))

# attrs: 원하는 태그 element 찾기
print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank02"})
print(rank1.a.get_text())

# # 형제 엘리먼트 간 이동:
# # next_sibling (다음 element로 이동)
# # rank2 = rank1.next_sibling.next_sibling   # 줄바꿈 으로 인해 두번 썻을때 다음 태그를 찾을수가 있엇다
# rank2 = rank1.find_next_sibling("li")   # find 를 활용해 다음 태그를 바로 찾기
# print(rank2.a.get_text())
# # previous_sibling (이전 element로 이동)
# # rank3 = rank2.previous_sibling.previous_sibling
# rank3 = rank2.find_previous_sibling("li")
# print(rank3.a.get_text())

# 형제 태그 전부 가져오기 ( sibling"s")
rank10 = rank1.find_next_siblings("li")
print(rank10)

# # .paret: 부모 태그 이동
# rank5 = (rank1.parent)
# print(rank5.li.get_text())

# # 텍스트로 찾기
# webtoon = soup.find("a", text="여신강림-174화")
# print(webtoon)
