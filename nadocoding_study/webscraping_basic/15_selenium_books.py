import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/books/collection/cluster?clp=sgIoCiAKGnByb21vdGlvbl9lYm9va190b3BzZWxsaW5nEEQYASIECAUILA%3D%3D:S:ANO1ljLtPtQ&gsr=CiuyAigKIAoacHJvbW90aW9uX2Vib29rX3RvcHNlbGxpbmcQRBgBIgQIBQgs:S:ANO1ljJFgfM"
headers = {
        "cookie": "_ga=GA1.3.289769616.1633458053; _gid=GA1.3.916551616.1633458053; OTZ=6185901_20_20__20_; 1P_JAR=2021-10-05-18; _gat_UA199959031=1; NID=511=lSiLKUgesCPCT0A16eklamEhzle1W0ShoMXfF1QZIbaTr8x4b1lYHau1x9Xzoqu9ZlYnQQUq1p_DkPAtKLLZ3v75szONEp9PrdTijOk2G7ziAF3cnMonRKafPhJeaMoIuJ3DwbBTotj3i4nTVCMaO_ko4E8O09bX32EzZSRZnTY",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
        "accept-language":"ko-KR,ko"    # 한글 페이지 요청
        }
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

movies = soup.find_all("div",attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))
print(movies)

# 읽어온 페이지 출력해보기
with open("movies.html","w",encoding="utf8") as f:
    # f.write((res.text))
    f.write(soup.prettify())    # html 문서를 예쁘게 출력

# 타이틀 가져오기
for movie in movies:
    title = movie.find("div",attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)