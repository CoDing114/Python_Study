import requests
url = "https://kimpga.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
print("ok")


with open("mykimp.html", "w", encoding="utf8") as f:
    f.write(res.text)

# 구글링 : user agent string

# 유저 에이젠트:
# 웹 사이트 에서는 헤더 정보를 통해 접속하는 사용자들의 정보를 알수가있다
# pc에서 접속 모바일에서 접속 등 과같이 접속 환경에 따라 보여지거나 차단할수도있다
# 헤더를 추가 활용하여 유저처럼 보일수있다
