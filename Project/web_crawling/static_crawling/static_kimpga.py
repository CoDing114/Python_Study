import requests
from bs4 import BeautifulSoup
import csv


# filename = "시가 총액1-200.csv"
# # 한글이 깨질때 사용가능    encoding="utf-8-sig"
# f = open(filename, "w", encoding="utf8", newline="")
# writer = csv.writer(f)

# title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split(
#     "\t")  # 탭으로 구분한 데이터 들이 리스트로 들어간다
# writer.writerow(title)

for page in range(1, 5):
    url = "https://kimpga.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    # 금융 정보 가져오기
    data_rows = soup.find("div", attrs={"class": "text-green"})
    print(data_rows)
    # for row in data_rows:
    #     columns = row.find_all("td")
    #     if len(columns) <= 1:  # 의미 없는 데이터는 skip
    #         continue
    #     # strip: 문자열 공백제거
    #     data = [column.get_text().strip() for column in columns]
    #     print(type(data))

    # writer.writerow(data)
