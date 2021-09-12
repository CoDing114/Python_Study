from tkinter import *
import tkinter.ttk as ttk  # 콘보 박스 불러오기

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")     # 가로 * 세로 크기 + x좌표 +y좌표

# 콤보 박스:
values = [str(i) + "일" for i in range(1, 32)]   # 1 ~ 31 일까지 숫가 를 일자로
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일 선택")    # 최초 목록 제목 설정

# state="readonly":읽기 전용
combobox2 = ttk.Combobox(root, height=10, values=values, state="readonly")
combobox2.pack()
combobox2.set("카드 결제일 선택")    # 최초 목록 제목 설정

# 인덱스 값 선택
combobox3 = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox3.current(0)    # 0 번째 인덱스 값 선택
combobox3.pack()


def btncmd():
    print(combobox.get())   # 선택 된값 표시
    print(combobox2.get())
    print(combobox3.get())


btn = Button(root, text="버튼", command=btncmd)
btn.pack()


root.mainloop()  # 창이 닫치지 않게 한다
