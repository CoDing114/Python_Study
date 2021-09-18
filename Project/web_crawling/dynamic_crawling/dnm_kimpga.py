from typing import Text
import requests     # http 요청을 보낼수 있다 pip install requests
import json
from openpyxl import Workbook  # 엑셀로 데이터 보낼때 사용 pip install openpyxl
import csv
from bs4 import BeautifulSoup


custom_header = {
    'referer': "https://kimpga.com/"
    'user-agent'
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
}

wb = Workbook
ws1 = wb.active
# ws1.append(["market", "kor_name", "eng_name"])

filename = "kimpga_v1.csv"
# 한글이 깨질때 사용가능    encoding="utf-8-sig"
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

title = "메이커	한글이름	영문이름	현재가	김프	전일대비	고가대비(52주)	저가대비(52주)	거래액(일)".split(
    "\t")  # 탭으로 구분한 데이터 들이 리스트로 들어간다
writer.writerow(title)


url = "https://api.upbit.com/v1/market/all"

req = requests.get(url, headers=custom_header)  # url에 연결
if req.status_code == requests.codes.ok:        # 연결 확인
    print("접속 성공")                           # 연결 되면 출력 아니면 에러
    stock_data = json.loads(req.text)           # 데이터 가져오기

for stock_dict in stock_data:                   # 데이터를 하나씩 받아오기

    # market = stock_dict["market"]               # key별로 value 분리
    # korean_name = stock_dict["korean_name"]
    # english_name = stock_dict["english_name"]
    # join_data = [market, korean_name, english_name]  # 분리한 value 조인
    # print(join_data)
    join_data = stock_dict["market"], stock_dict["korean_name"], stock_dict["english_name"]

    writer.writerow(join_data)
