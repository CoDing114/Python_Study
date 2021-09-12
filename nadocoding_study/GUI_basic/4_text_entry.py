from tkinter import *

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("640x480")    # 가로 * 세로 크기

# 텍스트
txt = Text(root, width=30, height=10)  # 텍스트 창 만들기
txt.pack()

txt.insert(END, "글자를 입력하세요")  # 안내 문구 작성

# 한줄 문구
e = Entry(root, width=30)   # Enter입력이 제한된다, [아이디 비번 입력으로 사용]
e.pack()
e.insert(0, "한줄만 입력해요")  # 현재는 값이 비어 있으므로 END를 써도 동일함


def btncmd():
    print(txt.get("1.0", END))  # 1:첫번째 라인, 0:0번쨰 column위치
    print(e.get())  # Entry값은 변수.get 으로만 적어 주면 된다

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫치지 않게 한다
