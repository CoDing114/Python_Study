import requests
res = requests.get("https://0433.tistory.com/")
# res.raise_for_status()
# print("ok")

print(len(res.text))
print("글자수:", res.text)

with open("mykimp.html", "w", encoding="utf8") as f:
    f.write(res.text)

# 유저 에이젠트:
# 웹 사이트 에서는 헤더 정보를 통해 접속하는 사용자들의 정보를 알수가있다
# pc에서 접속 모바일에서 접속 등 과같이 접속 환경에 따라 보여지거나 차단할수도있다
