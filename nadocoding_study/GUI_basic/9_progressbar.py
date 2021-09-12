from tkinter import *
import tkinter.ttk as ttk  # 프로그레스바 불러오기
import time  # 시간 불러오기

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")     # 가로 * 세로 크기 + x좌표 +y좌표

# 프로그레스바 ( 진행 상태 표시바 )
# mode:indeterminate(완복),determinate(0~100)
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10)   # 10ms 마다 움직임
progressbar.pack()


def btncmd():
    progressbar.stop()


btn = Button(root, text="중지", command=btncmd)
btn.pack()

# 상태바 만들어 보기
p_bar2 = DoubleVar()  # 실수도 가능 하기 위해 떠블 선택
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_bar2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):  # 1~100
        time.sleep(0.1)     # 0.1초 대기

        p_bar2.set(i)           # progressbar 의 값 설정
        progressbar2.update()   # UI 업데이트 시각화


btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()


root.mainloop()  # 창이 닫치지 않게 한다
