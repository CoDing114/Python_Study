from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")     # 가로 * 세로 크기 + x좌표 +y좌표

# 체크 박스
# 체크박스엔 variable을 설정해야한다. 체크 박스의 값을 저장 (변수에 저장)
chkvar = IntVar()  # chkvar에 int 형 으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select()   # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2)
chkbox2.pack()

# 버튼 클릭시 값 가져오기


def btncmd():
    print(chkvar.get())  # 0: 체크 해제, 1: 체크
    print(chkvar2.get())


btn = Button(root, text="버튼", command=btncmd)
btn.pack()


root.mainloop()  # 창이 닫치지 않게 한다
