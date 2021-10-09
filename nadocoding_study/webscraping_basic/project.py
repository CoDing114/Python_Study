import re
import requests
from bs4 import BeautifulSoup


# [오늘의 날씨]
# 흐림, 어제보다 00° 높아요
# 현재 00° (최저 00° / 최고 00°)
# 오전 강수확률 00% / 오후 강수확율 00%

# 미세먼지 00㎍/m³ 좋음
# 초미세먼지 00㎍/m³ 좋음
def create_soup(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    'cookie': 'JSESSIONID=F21FE788B337F0DF4A5E24678B1B4B97; NNB=FBS2CIBUMTCWA; _ga_1BVHGNLQKG=GS1.1.1623549022.1.1.1623549994.0; _ga=GA1.2.874199498.1623549023; ASID=7a2b546f0000017b5c417b7b00000060; NDARK=Y; nx_ssl=2; paneOrderNewsHome=today_main_news%2Csection_politics%2Csection_economy%2Csection_society%2Csection_life%2Csection_world%2Csection_it; page_uid=hTvBxlp0JXVssAwe68RssssstOZ-290770; NV_WETR_LOCATION_RGN_M="MDk3NDA2NDA="; NV_WETR_LAST_ACCESS_RGN_M="MDk3NDA2NDA="'
    }
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def print_news(index,title,link):
    print("{}.{}".format(index+1,title))
    print("  (링크 :{}".format(link))
def scrape_weather():
    print("[ 오늘의 날씨 ]")
    url = "https://weather.naver.com/today/09740640?targetId=compare"
    soup = create_soup(url)
    # print(soup)
    # 흐림,어제보다 00° 높아요
    cast = soup.find("p",attrs={"class":"summary"}).get_text().replace("\n", "")
    # 현재 00° (최저 00° / 최고 00°)
    curr_temp = soup.find("strong",attrs={"class":"current"}).get_text()    #.replace("도씨", "")
    min_temp = soup.find("span",attrs={"class":"data lowest"}).get_text().replace("평균기온", "기온:")
    max_temp = soup.find("span",attrs={"class":"data highest"}).get_text().replace("평균기온", "기온:")
    # 오전 강수확률 00% / 오후 강수확율 00%
    rain_rate = soup.find("dd",attrs={"class":"desc"}).get_text()    #.replace("도씨", "")
    # 미세먼지 00㎍/m³ 좋음
    fine_dust = soup.find_all("li",attrs={"class":"item_today level4_1"})[0].get_text().replace("\n", "")
    # 초미세먼지 00㎍/m³ 좋음
    ultra_fine_dust = soup.find_all("li",attrs={"class":"item_today level4_1"})[1].get_text().replace("\n", "")     #.replace("도씨", "")
    print(cast)
    print("{0}(최저 {1} / 최고 {2})".format(curr_temp,min_temp,max_temp))
    print("오전 강수확률"+rain_rate)
    print(fine_dust)
    print(ultra_fine_dust)
    
# [ 헤드라인 뉴스]
# 1. 타이틀
# ( 링크 )
# 2. 타이틀
# ( 링크 )
# 3. 타이틀
# ( 링크 )
def scrape_headline_news():
    print("헤드라인 뉴스")
    url = "https://news.naver.com"
    soup = create_soup(url)
    # print(soup)
    news_list = soup.find("ul",attrs={"class":"hdline_article_list"}).find_all("li",limit=30) # limit 수량만큼만 찾는다
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()    # news.div.a.get_text()
        link = url + news.find("a")["href"]
        print_news(index,title,link)
    print

def scrape_it_news():
    print("IT뉴스")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    # print(soup)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=30)
    # print(news_list)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 1번째 a 태그의 정보를 사용
        
        a_tag = news.find_all("a")[a_idx]
        try:
            title = a_tag.get_text().strip()
            link = a_tag["href"]
        except:
            print("잘못된 정보")
            continue
        print_news(index,title,link)
    print()

    # # 읽어온 페이지 출력해보기
    # with open("check".html","w",encoding="utf8") as f:
    #     # f.write((res.text))
    #     f.write(soup.prettify())    # html 문서를 예쁘게 출력

def scrape_english():
    print("오늘의 영어 회화")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")}) # 
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:  # 8문잔 잇다고 가정햇을때, index기준 4~7까지 잘라서 가져온다
        print(sentence.get_text().strip())
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())

if __name__ == '__main__':
    scrape_weather()    # 오늘의 날씨 정보 가져오기
    scrape_headline_news()  # 헤드라인 뉴스
    scrape_it_news()    # IT 뉴스
    scrape_english()    # 오늘의 영어 회화