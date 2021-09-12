from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정

# 버튼 설정
btn1 = Button(root, text="버튼1")   # root에 버튼 추가
btn1.pack()  # .pack으로 버튼 호출

btn2 = Button(root, padx=5, pady=10, text="버튼2")   # padx (패딩x) pady(패딩y)
btn2.pack()  # .pack으로 버튼 호출

btn3 = Button(root, padx=10, pady=5, text="버튼3")   # padx (패딩x) pady(패딩y)
btn3.pack()  # .pack으로 버튼 호출

btn4 = Button(root, width=10, height=5, text="버튼4")   # width,height 고정된 너비와 높이
btn4.pack()  # .pack으로 버튼 호출

btn5 = Button(root, fg="red", bg="yellow", text="버튼4")  # fg(컬러) bg(백그라운드 컬러)
btn5.pack()  # .pack으로 버튼 호출

photo = PhotoImage(file="image/1.png")  # 이미지 버튼
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("버튼이 클릭되었습니다")


btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()  # 창이 닫치지 않게 한다
