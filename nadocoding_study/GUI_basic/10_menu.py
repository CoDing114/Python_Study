from tkinter import *


root = Tk()
root.title("Rilla GUI")  # 이름 설정
root.geometry("340x480+1200+100")     # 가로 * 세로 크기 + x좌표 +y좌표

# 메뉴


def create_new_file():
    print("새 파일을 만듭니다")


menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()   # 구분자 삽입
menu_file.add_command(label="Open File")
menu_file.add_separator()   # 구분자 삽입
menu_file.add_command(label="Save All", state="disable")    # 비활성화
menu_file.add_separator()   # 구분자 삽입
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)  # 메뉴 타이틀

# Edit 메뉴 (빈값)
menu.add_cascade(label="Edit")

# Language 메뉴 추가 ( radio 버튼 기능을 통해 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴 ( 체크 버튼 기능 활용 )
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show List")
menu_view.add_checkbutton(label="Show Check")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)  # 메뉴 구성
root.mainloop()  # 창이 닫치지 않게 한다
