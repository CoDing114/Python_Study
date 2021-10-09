import requests  # 第三方数据请求模块 pip install requests
import re  # 正规表达式模块 内置模块
from selenium import webdriver  # pip install selenium
import time
from bs4 import BeautifulSoup
import csv
import os

url = "https://www.douyin.com/user/MS4wLjABAAAAgOeOms9eDZosgQd4dUMrxsD53sNhj7q3LA-nqqU0KQs6YUD0H5_OVJmzE6YIVXDK"
headers = {
    'cookie': 'douyin.com; MONITOR_DEVICE_ID=b9f7f768-9998-458a-946e-eae88e45b0a5; ttwid=1%7CV9ucG2YZiqdFxbN79OT86yWruuao5F8nKG2WKvICGwg%7C1633567140%7Ca06b95658378d3404bda72b9bc0a6e51c65331fe2bfcf83b462ae6b3d4ead835; _tea_utm_cache_6383=undefined; MONITOR_WEB_ID=9921f41a-68a6-41ce-a132-c05a06a3970f; _tea_utm_cache_2018=undefined; s_v_web_id=verify_69f60affd4e02fca1fcf7b91f119ebd2; msToken=tc_onyoRgBOUyqr8zLQAqPkmHQ2EgUzRZ8IhYqEtPNakrNSe9pFx61cgIoNiOn-EIKXhfcn_82Wdx-LWNnqI1vCk8CHEi7_rwyU7ErByA2h8fH31MFZymg==; ttcid=d81321ecb1bb4733b98f8be6c5fe8a2831; tt_scid=gm4raqPNys2ELW7arcNFV9jtLqIlToAu8B.TgCI5R2lqqG7Ey8DJV4O2G5t3anSF36d7; passport_csrf_token_default=55eddf8f748ea25e1fcf77bd5b4e5f2e; passport_csrf_token=55eddf8f748ea25e1fcf77bd5b4e5f2e; __ac_nonce=0615e4233005c258bbb7b; __ac_signature=_02B4Z6wo00f011.QJVgAAIDD39LfG5gFBadf8AHAALa1llfYNZnQORWr9vP3VNhL5dPuQ-WgE6oZkpl0TvgEM531UJM8UZaBFa4ORjQk1PC-qe4o6HDImwCbNVxAe03oEh9Brp57CLcQrBTmbe; __ac_referer=__ac_blank',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    # 'accept-language': 'ko,zh-CN;q=0.9,zh;q=0.8',
    # 'sec-fetch-site': 'none'
    }

# 비디오 데이터 저장 하기
# 정보 가져오기
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(soup)
title = soup.find("title").text
title = re.sub(r'[\/\\\:\*\?\"\<\>\|]', "_", title) # 파일명으로 쓸수없는 기호 수정
# title = re.sub("- 抖音", "#抖音", title) # 파일명으로 쓸수없는 기호 수정
print(title)
data_rows = soup.find("meta", attrs={"name": "description"})
print(data_rows)

# 폴더 만들기
path = './'+title
os.makedirs(path, exist_ok=True)

# 데이터 저장
filename = title+".csv"
# 한글이 깨질때 사용가능    encoding="utf-8-sig"
f = open(title+'\\'+ filename, "w", encoding="utf_8_sig")    # , newline="" 줄바꿈 없이기
writer = csv.writer(f)

a1 = [title]
writer.writerow(a1)
b1 = [url]
writer.writerow(b1)
data = [data_rows]
writer.writerow(data)
# strip: 문자열 공백제거
# data = ([title+"\n",url+"\n",data_rows])
print(type(data))
# print(data)
f.close()
print("데이터 저장 완료")

# 화면 스크롤
def drop_down():
    '''执行页面滚动操作'''  # javascript
    for x in range(2, 30, 2):  # 在你不断地下拉过程中,页面高度会变
        time.sleep(2)
        j = x / 9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver = webdriver.Chrome('D:\Downloads\coding\chromedriver.exe')  # 实例化浏览器对象
driver.get(url)
time.sleep(5)
drop_down()
print("스크롤 완료")



# 通过css语法 批量提取 li 标签 返回列表 元素对象
lis = driver.find_elements_by_css_selector('#root > div > div:nth-child(2) > div > div._67f6d320f692f9e5f19d66f4c8a1ecf9-scss > div._927ae3b0dd790b5b62eae61c7d2fa0bc-scss > div:nth-child(2) > ul > li')
# print(lis)
# 获取li标签
for li in lis:
    # 调用css 解析方法
    href = li.find_element_by_css_selector('a').get_attribute('href')
    # print(href)

    response = requests.get(url=href, headers=headers)
    # print(response.text)
    video_soup = BeautifulSoup(response.text, "lxml")
    # print(video_soup)

    video_title = re.findall('<title data-react-helmet="true">(.*?)</title>',response.text)[0]
    video_title = re.sub(r'[\/\\\:\*\?\"\<\>\|]', "_", video_title)
    video_title = re.sub("- 抖音", "#抖音", video_title) # 파일명으로 쓸수없는 기호 수정

    # 添加 try except 跳过异常
    try:
        href = re.findall('src(.*?)vr%3D%2', response.text)[1]
    except:
        print("list index out of range")
        continue
    video_url = requests.utils.unquote(href).replace('":"', 'https:')
    # response.content 获取二进制数据内容(因为保存图片/视频/音频/特定格式的文件 都是二进制数据保存)
    video_content = requests.get(url=video_url, headers=headers).content
    with open(title+'\\' + video_title + '.mp4', mode='wb') as f:
        f.write(video_content)
    print(video_title)
    # print(href)
    # print(video_url)
    

driver.quit()
