from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정

# 창설정:
# root.geometry("640x480")    # 가로 * 세로 크기
root.geometry("340x480+1200+100")    # 가로 * 세로 크기 + x좌표 +y좌표
# root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가(창 크기 변경 불가)

root.mainloop()  # 창이 닫치지 않게 한다
