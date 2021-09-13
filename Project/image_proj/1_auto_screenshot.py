import time
from PIL import ImageGrab

time.sleep(5)  # 5초 대기: 사용자 준비 시간

for i in range(1, 11):    # 10 개 이미지 저장
    img = ImageGrab.grab()  # 현재 스크린 이미지를 가져옴
    img.save("image{0}.png", format(i))  # 파일 저장 (image1.png ~ image10.png)
    time.sleep(2)   # 1초 단위
