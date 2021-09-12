from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")     # 가로 * 세로 크기 + x좌표 +y좌표

# 라디오 버튼 (여러개 버튼 중에서 선택 하는 버튼)
Label(root, text="메뉴르 선택하세요").pack()

# variable을 설정해야한다. 체크 박스의 값을 저장 (변수에 저장) (여러 번튼을 묶어서 사용가능)
burger_var = IntVar()   # chkvar에 int 형 으로 값을 저장한다.
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()  # 기본 값 설정
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="환타", value="환타", variable=drink_var)
btn_drink3 = Radiobutton(root, text="홍차", value="홍차", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get())  # 버거중 선택된 라디오 항목 값(value) 출력
    print(drink_var.get())  # 음료중 선택된 값 출력


btn = Button(root, text="버튼", command=btncmd)
btn.pack()


root.mainloop()  # 창이 닫치지 않게 한다
