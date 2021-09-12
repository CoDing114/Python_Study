from tkinter import *
import tkinter.messagebox as msgbox  # 메세지 박스 불러오기

root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")     # 가로 * 세로 크기 + x좌표 +y좌표

# 메세지 박스 ( 설정에 따라 해당 메세지 보여자기 )

# 기차 예매 시스템이라고 가정


def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")


def warn():
    msgbox.showinfo("경고", "해당 좌석은 매진 되었습니다.")


def error():
    msgbox.showerror("에러", "결제 오류가 방생 했습니다.")


def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매 하시겠습니까?")


def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적 오류입니다. 다시 시도 하시겠습니까?")


def yesno():
    msgbox.askyesno("예 / 아니요", "해당 좌석은 역방향입니다. 예매 하시겠습니까?")


def yesnocancel():
    response = msgbox.askyesnocancel(
        title=None, message="예매 내역이 저장 되지 않았습니다. 저장후 종료 하시겠습니까?")
    # yes: 저장후 종료
    # no: 저장 하지 않고 종료
    # cancel: 프로그램 종료 취소 (현재 화면 유지)
    print("응답:", response)    # True, False, None -> 예 1, 아니요0, 그외
    if response == 1:   # yes
        print("예")
    elif response == 0:  # no
        print("아니요")
    else:
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니요").pack()
Button(root, command=yesnocancel, text="예 아니요 취소").pack()


root.mainloop()  # 창이 닫치지 않게 한다
