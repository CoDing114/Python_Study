import requests  # 第三方数据请求模块 pip install requests
import re  # 正规表达式模块 内置模块
from selenium import webdriver  # pip install selenium
import time



def drop_down():
    '''执行页面滚动操作'''  # javascript
    for x in range(1, 30, 4):  # 在你不断地下拉过程中,页面高度会变
        time.sleep(2)
        j = x / 9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver = webdriver.Chrome('D:\Downloads\coding\chromedriver.exe')  # 实例化浏览器对象
driver.get('https://www.douyin.com/user/MS4wLjABAAAAvOU5GclmETa4jehXAEspnMfYJQZAbwcJzfUFhZk4cP8')
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

    headers = {
        'cookie': 'douyin.com; ttwid=1%7Cjf3oEBDRWDhAY7jUZZPd65SveMstsiLp0BN_dCZ_cUg%7C1633059331%7C829b6e8b8788ec4ee2495eefe6fb43dcfe2eaab4077b5caeec45ed122213c988; MONITOR_WEB_ID=50239bb2-6b9b-496c-90bf-6502948ad221; _tea_utm_cache_6383=undefined; passport_csrf_token_default=dcff7650cd75eba46e66547b98186986; passport_csrf_token=dcff7650cd75eba46e66547b98186986; ttcid=405c751f528f47f691371a33ce5fa73540; n_mh=RxZ96r-fRYrXy7RFX1JwwMNzmyRaK0JUztOPZ6y5R1c; sso_uid_tt=4d9a6e18525243ea1bb0bbf494628e4d; sso_uid_tt_ss=4d9a6e18525243ea1bb0bbf494628e4d; toutiao_sso_user=5691c8e6af0b707e5ba5f8ce75a3d673; toutiao_sso_user_ss=5691c8e6af0b707e5ba5f8ce75a3d673; uid_tt=4d9a6e18525243ea1bb0bbf494628e4d; uid_tt_ss=4d9a6e18525243ea1bb0bbf494628e4d; sid_tt=5691c8e6af0b707e5ba5f8ce75a3d673; sessionid=5691c8e6af0b707e5ba5f8ce75a3d673; sessionid_ss=5691c8e6af0b707e5ba5f8ce75a3d673; sid_guard=5691c8e6af0b707e5ba5f8ce75a3d673%7C1633060387%7C5183985%7CTue%2C+30-Nov-2021+03%3A52%3A52+GMT; odin_tt=6070a41b2cb4c316825907755499d288fe62bf39c271a97b5fa4f3fd030abc83150b4bef3eda494938121cf3cdd88e06; _tea_utm_cache_2018=undefined; MONITOR_DEVICE_ID=c3605643-db4f-4391-843a-4bd080cf1f81; msToken=QkvjB2mVY3-3eH7Ootw4wIhaswCss_zmaMg8m10HY46wG3xKcgF88NL-2Xyzk8LrKD5Ktf4s7fVe__LRAiQvQGaTx8oPTb2Vv9sBXz3Von7OjOqcnDyuq9w=; douyin.com; msToken=H-1PvOkoiTPLORcaaAjjzuUzrNOLNXsJ_mFu0LekpxwYM42YqUMpdDgDkyeu_iEa73umf50b8227ZKEJWeFYSprNYCfJyhUDTMQ1N8OaHz1CIJqJ6xn7aTc=; tt_scid=JBdE.tY-12STcY5yxRddT-9cmkABGD0HYtu9.57I7-VHpSS6dxrqIc-uMWYEvRGreafe; __ac_nonce=0615dea9e009c95cfa6f0; __ac_signature=_02B4Z6wo00f01NCwUmQAAIDAjoWhEHdnW2TQlFbAAFV3a8rguBuM1BfFE7b8dXd-rlV20vZohaBnEqoeTGiQvmYId.RYCYNsVONUqLn9BPxPjlNVjs2gb5uy.NJ37wSwO-yY-vt.eMHow-2y37; __ac_referer=__ac_blank',
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

driver.quit()
