import requests  # 第三方数据请求模块 pip install requests
import re  # 正规表达式模块 内置模块
from selenium import webdriver  # pip install selenium
import time


def drop_down():
    '''执行页面滚动操作'''  # javascript
    for x in range(1, 30, 4):  # 在你不断地下拉过程中,页面高度会变
        time.sleep(1)
        j = x / 9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver = webdriver.Chrome('D:\Downloads\chromedriver.exe')  # 实例化浏览器对象
driver.get('https://www.douyin.com/user/MS4wLjABAAAAX9Yu0jmn_mGK0EAWKP7nJ49OStJ3gy3Vc_a0F81rMaUa3SRGFNmm2MZP2wGZPuSD')
time.sleep(3)
drop_down()

# 通过css语法 批量提取 li 标签 返回列表 元素对象
lis = driver.find_elements_by_css_selector('#root > div > div:nth-child(2) > div > div._67f6d320f692f9e5f19d66f4c8a1ecf9-scss > div._927ae3b0dd790b5b62eae61c7d2fa0bc-scss > div:nth-child(2) > ul > li')
# print(lis)
# 获取li标签
for li in lis:
    # 调用css 解析方法
    href = li.find_element_by_css_selector('a').get_attribute('href')
    print(href)

    # url = 'https://www.douyin.com/video/7013943353687526670'
    headers = {
        'cookie': 'douyin.com; MONITOR_DEVICE_ID=720e864d-040d-47c8-93f9-1a2c6150fad4; ttcid=f7f9e0bdeaf346eca7312dff0bf942e331; ttwid=1%7C0rfjFX0qP0BEqRw8qQgsZw61UxjgYOPDyiLcuuX4Jao%7C1633172131%7C18310c5b2b7188be8ff944c9a07b1e59c6075eed6e58b9f8036135033b064a62; _tea_utm_cache_6383=undefined; MONITOR_WEB_ID=aa2d0200-5db2-438e-927c-76b674ace5a1; s_v_web_id=verify_a42976d1dfdc9a6f6bab48d1b604c73b; _tea_utm_cache_2018=undefined; tt_scid=fGmXMBkNeh0KWnGY03ElJWP-6ksxesJTBNDzO16v4YT1clx76yL3bA2Ki4kZmZDce3c3; passport_csrf_token_default=8e373b034ece2ea014ec8f533ff001e0; passport_csrf_token=8e373b034ece2ea014ec8f533ff001e0; msToken=0HF0HeusVxvpR9WvnLrY3b_GVzxz3drlw6-lCKgpQKyZrZZCbm3J1_bhXAk8bodtY4VIe__ea81Xl4qM5ofd3JZ2K22VqBS47Y-ABVh5Ckije4Nk4GHVG5Hm; __ac_nonce=0615845cf00b5ba25fcbb; __ac_signature=_02B4Z6wo00f01uhZgZAAAIDCaFt70OVYQFboeaUAANtbWmA6.yCTrVXx6or.n432f3Y7rVSbeJFIqI6gaciqwX9UcMVGJoafd4uizI.G9rWKdfwlOJrdMNM4W81QGW6TX4X1EHrv7iWqkiqBfb; __ac_referer=https://www.douyin.com/user/MS4wLjABAAAAX9Yu0jmn_mGK0EAWKP7nJ49OStJ3gy3Vc_a0F81rMaUa3SRGFNmm2MZP2wGZPuSD',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }

    response = requests.get(url=href, headers=headers)
    print(response.text)

    title = re.findall('<title data-react-helmet="true">(.*?)</title>',response.text)[0]
    title = re.sub(r'[\/\\\:\*\?\"\<\>\|]', "_", title)
    href = re.findall('src(.*?)vr%3D%2', response.text)[1]
    video_url = requests.utils.unquote(href).replace('":"', 'https:')
    # response.content 获取二进制数据内容(因为保存图片/视频/音频/特定格式的文件 都是二进制数据保存)
    video_content = requests.get(url=video_url, headers=headers).content
    with open('video\\' + title + '.mp4', mode='wb') as f:
        f.write(video_content)
    print(title)
    # print(href)
    print(video_url)

# driver.quit()
