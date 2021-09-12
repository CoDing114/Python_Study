from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")    # 가로 * 세로 크기 + x좌표 +y좌표

# 스크롤바 [ 스크롤바와 스크롤바 대상을 같은 프레임에 넣고 관리하는 것이 편하다]
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스로롤을 내려도 무반응 다시 올라옴
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):   # 1 ~ 31 일
    listbox.insert(END, str(i) + "일")  # 1일,2일,...
listbox.pack(side="left",)

scrollbar.config(command=listbox.yview)  # 스크롤바를 리스트 박스에 맵핑
root.mainloop()  # 창이 닫치지 않게 한다
