# 1. 截图保存图片
# 2. 识别图片上面的文字

# 0. 导入库 pip install "keyboard"
import keyboard #如果是3.6(python)以上版本，可能支持不是很好
from PIL import ImageGrab   # pip install pillow
import time

# 1.截图
keyboard.wait(hotkey='F1')
print('f1 ok')
keyboard.wait(hotkey='ctrl+c')
print('ctrl+c ok')
time.sleep(1)

# 2.保存图片到电脑上
image = ImageGrab.grabclipboard()   #从剪贴板里面获取图片
image.save('001.png')

# 3.识别图片上的文字 （OCR）
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '24778882'
API_KEY = 'yVdBDHTrbkk5dYBoIjXONvQI'
SECRET_KEY = 'Ke1vLR3BK9ae9mRfs3C8A8AHRkViCGXy'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('001.png')

""" 调用通用文字识别（高精度版） """
text = client.basicAccurate(image);
print(text)