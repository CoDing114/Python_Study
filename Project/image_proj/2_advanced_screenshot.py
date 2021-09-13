import keyboard
import time
from PIL import ImageGrab


def screeshot():
    curr_time = time.strftime("_%Y%m%d_$H%M%S")
    img = ImageGrab.grab()
    img.save("image{0}.png".format(curr_time))


keyboard.add_hotkey("F9", screeshot)    # F9 스크린샷

keyboard.wait("esc")    # esc 누를기 전까지 실행
