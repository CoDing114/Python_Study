from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")    # 가로 * 세로 크기 + x좌표 +y좌표

Label(root, text="메뉴를 선택해 주세요").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")
# 프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="한우버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 제목 있는 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="홍차").pack()
Button(frame_drink, text="녹차").pack()


root.mainloop()  # 창이 닫치지 않게 한다
