from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("640x480")    # 가로 * 세로 크기

# 리스트 박스
# selectmode: 선택가능 모드(single:하나만 선택 가능) height표시 개수(0: 전부)
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # 삭제: 순서 설정[0: 맨 앞에서 삭제], [END: 맨뒤에서 삭제]
    listbox.delete(END)


def btn2cmd():
    # 갯수 확인:
    print("리스트에는", listbox.size(), "개가 있어요")


def btn3cmd():
    # 할목 확인:(시작 idx, 끝 idx)
    print("1번째 부터 3번째까지의 항목:", listbox.get(0, 2))


def btn5cmd():
    # 선택된 항목 확인 (index값을 반환해준다(위치 값:ex)(1,2,3))
    print("선택된 항목:", listbox.curselection())


def btn6cmd():
    # 선택항목 삭제 (하나씩만 삭제 가능)
    deld = listbox.curselection()
    listbox.delete(deld)


btn = Button(root, text="삭제", command=btncmd)
btn.pack()
btn2 = Button(root, text="개수 확인", command=btn2cmd)
btn2.pack()
btn3 = Button(root, text="항목 확인", command=btn3cmd)
btn3.pack()
btn5 = Button(root, text="위치 확인", command=btn5cmd)
btn5.pack()
btn6 = Button(root, text="선택 삭제", command=btn6cmd)
btn6.pack()

root.mainloop()  # 창이 닫치지 않게 한다
