from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정

# label은 글자나 이미지를 보여준다

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="image/1.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")  # 버튼 클릭시 label1 "또만나요" 로 바뀐다

    # Garbage Clooection: 불필요한 메모리 공간 해제
    # 함수내에서 이미지 값 등을 바꾸기 위해서는 전역변수로 만들어 줘야한다
    global photo2   # 글로벌 전역 변수로 만들어준다
    photo2 = PhotoImage(file="image/2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()  # 창이 닫치지 않게 한다
