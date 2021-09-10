# 파일에 데이터 쓰기
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 60", file=score_file)
score_file.close()
