import requests  # 第三方数据请求模块 pip install requests
import re  # 正规表达式模块 内置模块
# from selenium import webdriver  # pip install selenium

url = 'https://www.douyin.com/video/7013943353687526670'
headers = {
    'cookie': 'douyin.com; ttwid=1%7Cjf3oEBDRWDhAY7jUZZPd65SveMstsiLp0BN_dCZ_cUg%7C1633059331%7C829b6e8b8788ec4ee2495eefe6fb43dcfe2eaab4077b5caeec45ed122213c988; douyin.com; MONITOR_WEB_ID=50239bb2-6b9b-496c-90bf-6502948ad221; _tea_utm_cache_6383=undefined; passport_csrf_token_default=dcff7650cd75eba46e66547b98186986; passport_csrf_token=dcff7650cd75eba46e66547b98186986; s_v_web_id=verify_ku7td4h9_h4XosaQE_ePZS_4CP2_939A_W6UGx7S4hX6w; ttcid=405c751f528f47f691371a33ce5fa73540; n_mh=RxZ96r-fRYrXy7RFX1JwwMNzmyRaK0JUztOPZ6y5R1c; sso_uid_tt=4d9a6e18525243ea1bb0bbf494628e4d; sso_uid_tt_ss=4d9a6e18525243ea1bb0bbf494628e4d; toutiao_sso_user=5691c8e6af0b707e5ba5f8ce75a3d673; toutiao_sso_user_ss=5691c8e6af0b707e5ba5f8ce75a3d673; uid_tt=4d9a6e18525243ea1bb0bbf494628e4d; uid_tt_ss=4d9a6e18525243ea1bb0bbf494628e4d; sid_tt=5691c8e6af0b707e5ba5f8ce75a3d673; sessionid=5691c8e6af0b707e5ba5f8ce75a3d673; sessionid_ss=5691c8e6af0b707e5ba5f8ce75a3d673; sid_guard=5691c8e6af0b707e5ba5f8ce75a3d673%7C1633060387%7C5183985%7CTue%2C+30-Nov-2021+03%3A52%3A52+GMT; odin_tt=6070a41b2cb4c316825907755499d288fe62bf39c271a97b5fa4f3fd030abc83150b4bef3eda494938121cf3cdd88e06; __ac_nonce=06156867600eb28e244f0; __ac_signature=_02B4Z6wo00f01qSXG-AAAIDC-qLolKAzeSKktx9AAMh.VUTq7jrODn9rOnOhIotJucYgaQ09LX6.NQbGD2M4LVC9QIwF.Hk3P7WI8fwHfVo-VMZ8jDh8oyJZQvZ2RCAX0c1JDYMazqsnfwyCd6; tt_scid=j828MIyErp3oJeR29mQhV6KU2sPzT.1bcTOAP8iT3d552OBswPwrNFg7W6wUeYn-a174; msToken=SrqPbKEeSPbbuzlO5EKKHUaSpCdrmi9WHU-x0A15mY8NbqHjaNZfYKk3xVWzS9KfQ07eoYQgkZm3tO0lOgFWIA-pxyi9uk73b5GLJnuuOmbqiXxFS6bjYGEK',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
print(response.text)

title = re.findall(
    '<title data-react-helmet="true"> (.*?)</title>', response.text)[0]
href = re.findall('src(.*?)vr%3D%2', response.text)[1]
video_url = requests.utils.unquote(href).replace('":"', 'https:')
# response.content 获取二进制数据内容(因为保存图片/视频/音频/特定格式的文件 都是二进制数据保存)
video_content = requests.get(url=video_url, headers=headers).content
with open('video\\' + title + '.mp4', mode='wb') as f:
    f.write(video_content)
print(title)
# print(href)
print(video_url)
