# 나도코딩 (기본편)
# # 1. 숫자 자료형
# 2. 문자열 자료형
# 3. boolean 자료형 [ True / False]
# 4. 변수
# 5. 연산자
import byme
import datetime
import time
import os
import glob
import random  # 외장함수
from bs4 import BeautifulSoup
import random   # 찾으려는 패키지 [random]
import inspect
from travel import *
from travel import vietnam
from travel.vietnam import VietnamPackage
import travel.thailand
import theater_module as mv  # 긴 이름 일경우 줄여서 사용가능
import pickle
from random import *
from math import *

print(1 + 1)  # 2
print(7 - 5)  # 2
print(2 * 3)  # 6
print(6 / 2)  # 3

print(2 ** 3)  # 2^3 = 8 승
print(5 % 3)  # 나머지 구하기 2
print(5 // 3)  # 몫 1

print(2 < 3)  # True
print(2 > 3)  # False

print(1 != 3)  # True 같지않다
print(not (1 != 3))  # False

print((2 < 3) and (2 > 3))  # False
print((2 < 3) & (2 > 3))  # False

print((2 < 3) or (2 > 3))  # True
print((2 < 3) | (2 > 3))  # True

# 6. 간단한 수식
print(" 6. 간단한 수식")
print(2 + 3 * 3)  # 11
print((2 + 3) * 3)  # 15
number = 2 + 3 * 3  # 11
print(number)
number = number + 2  # 13
print(number)
number += 2  # 15
print(number)

# 7. 숫자 처리 함수
print("7. 숫자 처리 함수")
print(abs(-5))  # 5 # 절대값
print(pow(4, 2))  # 4^2 = 16
print(max(5, 12))  # 12 최대값
print(min(5, 12))  # 5  최저값
print(round(3.33))  # 3 반올림

# from math import *
print(floor(4.99))  # 4  내림.
print(ceil(3.14))  # 4  올림.
print(sqrt(16))  # 4 제곱근.

# 8. 랜덤 함수
print("# 8. 랜덤 함수")
# from random import *
print(random())  # 0.0 ~ 1.0
print(random() * 10)  # 0.0 ~ 10.0
print(int(random() * 10))  # 0.0 ~ 10.0
print(int(random() * 10) + 1)  # 0.0 ~ 10.0
print(randrange(1, 11))  # 0.0 ~ 10.0
print(randint(1, 10))  # 0.0 ~ 10.0

# 9. 문자열
print("""큰
따옴표
세개로
줄바꿈
 """)
# 10.슬라이싱
jumin = "221021-12324567"
print("생년월일:" + jumin[:6])  # 생년월일:221021
print("뒤7자리:" + jumin[7:])  # 뒤7자리:12324567
print("뒤7자리(뒤에서부터):" + jumin[-8:])  # 뒤7자리(뒤에서부터):12324567

# 11. 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())  # 소문자
print(python.upper())  # 대문자
print(python[0].isupper())  # 첫문자 대문자인지 체크
print(len(python))  # 문자 길이
print(python.replace("Python", "Java"))  # 문자 바꾸기

index = python.index("n")  # 글자 시작 위치 찾기
print(index)

index = python.index("n", index + 1)  # 글자 찾기 위치 포지션 +1
print(index)

print(python.find("Java"))  # 찾으려는 문자가 없을때 -1을 반환한다

# 12. 문자열 포맷
# print("a","b")
# print("a"+"b")

# 방법 1
print("나는 %d 살입니다" % 20)  # 숫자를 받아온다
print("나는 %s을 좋아합니다" % "파이썬")  # 문자르 받아온다
print("Apple은 %c로 시작해요" % "A")  # 캐릭터를 받아온다 [1]
print("나는 %s과 %s를 좋아해요" % ("Python", "Java"))

# 방법 2
print("나는 {}살 입니다".format(20))
print("나는 {1}과 {0}를 좋아해요".format("Python", "Java"))

# 방법 3
print("나는 {age}살이며, {prg}을 좋아해요".format(age=20, prg="Python"))

# 방법 4 (3.6 이상~)
age = 20
prg = "python"
print(f"나는 {age}살이며, {prg}을 좋아해요")

# 4.5 탈출 문자
# \n :줄 바꿈
print("문장 \n 줄 바꿈")

# \": 문장내 \" \' 따옴표
print("저는 '코릴라' 입니다")
print("저는 \"코릴라\" 입니다")

# \\: 문장내 역슬러시 \
print("C:\\Bitnami\\wampstack-8.0.8-0\\apache2\\htdocs> ")  # 역슬러시 두개를 하나로 간주

# \r: 커서 맨 앞으로 이동
print("Red Apple\rPine")

# \b: 백스페이스 (한글자 삭제)
print("Redd\b Aapple")

# \t : Tap 탭
print("Red\tApple")

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 5-1 리스트

# subway1 = 10
# subway2 = 20
# subway3 = 30
subway = [10, 20, 30]
print(subway)

# 데이터 파인드
print(subway.index(20))

# 데이터 추가
subway.append(50)
print(subway)

# 원하는 위치에 데이터 추가
subway.insert(3, 66)
print(subway)

# 뒤에서 하나씩 빼기
print(subway.pop())
print(subway)

# 같은 데이터 몇개 잇는지 찾기
subway.append(20)
print(subway)
print(subway.count(20))

# 데이터 순서 정렬
subway.sort()
print(subway)

# 데이터 순서 뒤집기
subway.reverse()
print(subway)

# 데이터 합치기
subway2 = [99, 88, 77]
subway.extend(subway2)
print(subway)

# 모두 지우기
subway.clear()
print(subway)

# 5-2 사전
cabinet = {1: 10, 2: 20}
print(cabinet)

# 사전에서 데이터 불러오기 방법 #1
print(cabinet[1])
# 사전에서 데이터 불러오기 방법 #2
print(cabinet.get(3))
# ** 방법#1[] 사용시 데이터 없으면 오류 발생, 방법#2 .get사용시 데이터 없으면 None 반환. **
print(cabinet.get(3, "사용 가능"))  # None 대신 원하는 데이터 대체 가능

# 사전에 지정 Key가 잇는지 확인 가능
print(1 in cabinet)  # True

# 값 추가 혹은 업데이트
cabinet[2] = 88
cabinet[3] = 66
print(cabinet)

# Key Dilete , key 삭제
del cabinet[1]
print(cabinet)

# Key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# Key,value 쌍으로 출력
print(cabinet.items())

# Key.Clear
cabinet.clear()
print(cabinet)

# 5-3
# 튜플() : 데이터 추가 업데이트 되지 않은 반면 속도가 빠르다
# name = "CoRilla"
# age = 20
# hobby = "Coding"
# print(name, age, hobby)
(name, age, hobby) = ("CoRilla", 20, "Coding")
print(name, age, hobby)

# 5-4 집합 (set)
# 중복 안됨, 순서 없음
java = {"rilla", "miki", "joker"}
python = {"rilla", "huke"}

# 교집합 (Java 와 Python을 모두 할수 잇는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (Java 혹은 Python 할수잇는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (Java 할수잇지만 python 못하는 개발자)
print(java - python)
print(java.difference(python))

# 데이터 추가 python 할수 잇는 사람 늘어남
python.add("joker")
print(python)

# 데이터 삭제
java.remove("joker")
print(java)

# 5-5 자료 구조 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 6 - 1 if 조건문
temp = (-30)
# temp = int(input("기온은어때요？"))
if 30 <= temp:
    print("너무더워요.나가지마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은날씨에요")
elif 0 <= temp < 10:
    print("외투를챙기세요")
else:
    print("너무추워요.나가지마세요")

# 6 - 2 for 반복문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# print("대기번호 : 5")
for waitiong_no in range(1, 6):  # [1,2,3,4,5]  # randrange()와 동일
    print("대기번호: {0}".format(waitiong_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer_st in starbucks:
    print("{0},커피가 준비 되었습니다.".format(customer_st))

# 6 - 3 while 반복문 어떤 조건이 만족될때까지 반복 2:09:33
# 예제1
customer_tr = "토르"
index_TR = 5
while index_TR >= 1:
    print("{0},커피가준비되었습니다.{1}번 남았어요.".format(customer_tr, index_TR))
    index_TR -= 1
    if index_TR == 0:
        print("커피는 폐기처분 되었습니다.")
# 예제2
# customer_rl = "릴라"
# person = "Unknown"
# while person != customer_rl:
#     print("{0}, 커피가 준비 되었습니다.".format(customer_rl))
#     person = input("이름이 어떻게 되세요")

# 6 - 4 Continue 와 break
# continue는 계속해서 다음 반복을 진행, break는 반복문을 종료하고 끝낸다
absent = [2, 5]  # 결석 2명
no_book = [7]
for student in range(1, 11):  # 1 부터 10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지,{0}는 옥상으로 따라와".format(student))
        break
    print("{0},책을 읽어봐".format(student))

# 한줄 for 문
# 예제1:
# 출석번호가 1,2,3,4, 앞에 100을 붙이기로 함 -> 101,102,103,104..
students_for = [1, 2, 3, 4, 5]
print(students_for)
# i에 100을 더하는데, i에 students_for의 값을 불러온다
students_for = [i + 100 for i in students_for]
print(students_for)

# 예제2:
# 학생 이름을 길이로 변환
student_len = ["Iron man", "Thor", "I am groot"]
# i값의 길이를 구하는데,i의 값은 student_len변수에서 가져온다
student_len = [len(i) for i in student_len]
print(student_len)

# 예제3
# 학생 이름을 대문자로 변환
student_upper = ["Iron man", "Thor", "I am groot"]
student_upper = [i.upper() for i in student_upper]
print(student_upper)


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 7 - 1 함수
# 함수를 정의할땐 def로 시작하며 함수 이름을 적고, 괄호() 열고 닫고 나서, 콜론":"으로 정의 하고나서 함수내에서 실제로 수행되는 내용을 작성 하면된다
# 함수 생성후엔 호출해줘야 실행 될수잇다


def open_account():  # 함수 정의
    print("새로운 계좌가 생성되었습니다")


open_account()  # 함수 호출


# 7 - 2 전달 값과 반환 값

# 예제1:


def deposit(balance, money):  # 입금
    print("입금이 완료 되었습니다. 잔액은 {0}원 입니다".format(balance + money))
    return balance + money


# 예제2:


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많을때
        print("출금이 완료 되었습니다. 잔액은 {0}원 입니다".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다.잔액은 {0}원 입니다".format(balance))
        return balance


# 예제3:


def withdraw_night(balance, money):  # 야간 출금
    commissin = 100  # 수수료 100원
    return commissin, balance - money - commissin


balance = 1000
balance1 = deposit(balance, 1000)  # deposit의 계산 결과를 반환받는다
balance2 = withdraw(balance, 5000)
balance2 = withdraw(balance, 200)
commissin, balance3 = withdraw_night(balance, 600)
print("야간 수수료는 {0}원 이며, 잔액은 {1}원 입니다.".format(commissin, balance3))
print(balance1)
print(balance2)
print(balance3)


# 7 - 3 기본 값
# 기본 값은 값이 있을땐 주어진값을 반환하지만 값이 없을땐 설정된 값을 반환한다
# def profile(name, age, main_lang):
#     print("이름:{0}\t나이:{1}\t언어:{2}"
#           .format(name, age, main_lang))


# profile("corilla", 20, "python")
# profile("miki", 20, "python")

def profile(name, age=20, main_lang="python"):
    print("이름:{0}\t나이:{1}\t언어:{2}"
          .format(name, age, main_lang))


profile("CoRilla")
profile("MIKI", 20, "Java")


# 7 - 4 키워드 값
# 키워드를 이용해서 함수를 호출해주면 순서와 상관없이 잘 전달 된다


def profile(name, age=20, main_lang="python"):
    print(name, age, main_lang)


profile(name="CoRilla", age=20, main_lang="python")
profile(age=20, main_lang="python", name="Miki")


# 7 - 5 가변 인자 를 이용한 함수 호출
# 가변인자 사용전:
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름:{0}\t나이:{1}\t".format(name, age), end="언어:")
#     print(lang1, lang2, lang3, lang4, lang5)


# profile("Corilla", 20, "python", "java", "C", "C++", "C#")
# profile("MIKI", 20, "python", "Java", " ", " ", " ")

# 가변인자 사용후:
def profile(name, age, *languages):
    print("이름:{0}\t나이:{1}\t".format(name, age), end="언어:")
    for lang in languages:
        print(lang, end=" ")
    print()


profile("Corilla", 20, "python", "java", "C", "C++", "C#")
profile("MIKI", 20, "python", "Java")


# 7 - 6 지역변수 완 전역변수
# 지역변수: 함수내에서만 쓸수잇다, 함수가 호출될때 만들어 졋다가 함수가 끝나면 사라진다
# 전역변수: 프로그램 내 모든 공간에서 사용가능

# 예제1: 지역변수만 사용


def checkpoint(soldiers):
    gun = 10  # 지역변수 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))


# 예제2: 전역변수인 글로벌 변수 불러오기
gun = 10


def checkpoint(soldiers):
    global gun  # 전역공간에 잇는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))


# 예제3: 전역 변수 및 리턴 [추천]
def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun


print("전체 총:{0}".format(gun))
checkpoint(2)  # 2명 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


# 8 - 1 표준 입출력
# sep="," 문단 구분기호
# end="?" 뒤 문장과 현문장 한문장으로 표현

# .items(): key 와 value를 불러온다
# ljust: 공강확보 및 왼쪽 정렬
# rjust: 공간확보 및 오른쪽 정렬
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(4), str(score).rjust(4), sep=":")

# .zfill(): 공간확보민 빈자리 0을 채운다
# 예제: 은행 대기순번표 001,002,003,...
for num in range(1, 21):
    print("대기번호:" + str(num).zfill(3))

# input: 사용자 입력(을 통해서 받게되면 항상 문자열 형식으로 저장된다)
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은" + answer + "입니다")

# 8 - 2 다양한 출력 포맷
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 빈자리는 $로 채워주기
print("{0:$>+18,}".format(2700000000))

# 소수점 출력 및 소수점 둘째 자리까지만 출력
print("{0:.2f}".format(5 / 3))  # 1.666667 > 1.67

# 8 - 3 파일 입출력
# 파일에 데이터 쓰기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 60", file=score_file)
# score_file.close()
#
# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일 데이터 읽기
# 예1: 전체 데이터 읽어오기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# 예2:한줄씩 읽어 오기
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# print(score_file.readline(),end=" ")
# score_file.close()

# 예3: while문으로 전체 데이터 불러오기
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()

# 예4: 리스트형태로 불러와서 출력할수있다
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.read()
# for line in lines:
#     print(line, end="")
# score_file.close()
# print()

# 8 - 4 pickle
# 프로그램 상에서 이용하고 잇는데이터를 파일 형태로 저장해준다. 읽을때 역시 피클을 사용하여 불러올수잇다
# write
# profile_file = open("profile.pickle", "wb")
# profile = {"name": "Rilla", "age": 20, "lang": ["Python", "Java"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file레 저장
# profile_file.close()
#
# # read
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()

# 8 - 5 with 편하게 데이터 읽고/쓰기
# pickle파일 읽어 올때
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))  # 위드를 사용하면 파일 close를 안해줘도 된다

# # txt 파일에 쓸때
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부중,,,")
#
# # txt 파일에 읽어 올때
# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 9-1.클래스
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("{0} 의 체력{1},공격력{2} 입니다".format(self.name, self.hp, self.damage))


# 9-2._init_
print("객체가 생성될땐 기본적으로 init 함수에 정의된 개수와 동일하게 설정해 줘야한다 (self 는 제외)")
marine1 = Unit("마린", 40, 5)  # Unit class 의 인스턴스 DB
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 9-3.멤버변수
print("클래스 내에서 정의 된 변수,그 변수를 가지구 초기화 할수잇구 실제로 쓸수도 있다")
# 레이스를 만들어 보자: 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력{1}".format(wraith1.name,
                                  wraith1.damage))  # 이런식으로 멤버 변수를 밖에서 쓸수잇다

# 외부에서 객체에 추가로 값을 만들어서 쓸수가 있다
# (이때 주의 할 점은 내가 확장한 객체에 대해서만 적용이 된다.기존에 있던 객체는 동일 하다)
# 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것 (뺴앗음)
wraith2 = Unit("레이스2", 80, 5)
wraith2.clocking = True

if wraith2.clocking:
    print("{0} 는 현재 클로킹 상태 입니다".format(wraith2.name))


# 9-4.메소드(Method)
# 메소드는 클래스에 포함 되어있는 함수를 가르킨다.
# 공격 유닛 만들기
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 처력은 {1} 입니다".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴 되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")  # AttackUnit 에 있는 attack 라는 함수를 호출한다

# 공격 2번 받는다고 가정
firebat1.damaged(25)  # AttackUnit 에 있는 damaged 라는 함수를 호출한다
firebat1.damaged(25)


# 9-5.상속
# 중복 되는 부분을 상속 받아 사용 할수잇다
class BasicUnit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class MpiUnit(BasicUnit):
    def __init__(self, name, hp, damage, mp):
        BasicUnit.__init__(self, name, hp)
        self.damage = damage
        self.mp = mp
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("{0} 의 체력{1},공격력{2}, 마나{3}입니다"
              .format(self.name, self.hp, self.damage, self.mp))


porking1 = MpiUnit("포킹", 40, 5, 20)


# 9-6.다중상속
# 공중 유닛 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도는 {2} 입니다"
              .format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableMpiUnit(MpiUnit, Flyable):
    def __init__(self, name, hp, damage, mp, flying_speed):
        MpiUnit.__init__(self, name, hp, damage, mp)
        Flyable.__init__(self, flying_speed)


# 발키리 : 공중 공격 유닛
valkyrie = FlyableMpiUnit("발키리", 200, 25, 20, 5)
valkyrie.fly(valkyrie.name, "3시")


# 9-7.메소드 오버라이딩(Overriding)과 super()
# 메소드 오버라이딩은 상속 관계에서 동일한 메소드가 있을 때 특정 클래스의 메소드를 무시하고, 다른 클래스의 메소드를 사용하는 방식 입니다. 오버라이딩은 기존에 이미 만들어진 메소드의 이름을 똑같이 만들어야할 때 사용 됩니다.
# 예를들어 아래와 같이 부모 클래스(parent_class)에 over 메소드가 있을 때 자식 클래스(child_class)에도 over라는 메소드가 필요하여 자식 클래스에 사용하게 되면 자식 클래스의 over 메소드가 호출 됩니다.
class parent_class:
    def over(self):
        print("부모 클래스의 over 메소드 입니다.")


class child_class(parent_class):
    def over(self):
        print("자식 클래스의 over 메소드 입니다.")


test = child_class()
test.over()


# 이렇게 동일한 이름의 메소드를 삽입했을 때 특정 클래스의 메소드가 무시되는걸 오버라이딩이라고 합니다.

# 만약, 필요에 의해 오버라이딩한 자식 클래스의 over 메소드를 삽입 했으나 부모 클래스의 over 메소드도 같이 필요하다면 super() 를 이용하시면 됩니다.
class parent_class:
    def over(self):
        print("부모 클래스의 over 메소드 입니다.")


class child_class(parent_class):
    def over(self):
        super().over()
        print("자식 클래스의 over 메소드 입니다.")


test = child_class()
test.over()


# 이렇게 super()를 이용할 경우 부모 클래스의 지정한 메소드를 호출하며, 오버라이딩된 상황에서 특정 메소드를 중복하여 출력하거나 값이 필요한 경우 사용될 수 있습니다.

# 9-8.pass
# 에러 없이 패스해 넘어간다
def game_start():
    print("[알림] 새로운 게임을 시작 합니다")


def game_over():
    pass


def game_restart():
    print("[알림] 게임을 재시작 합니다")


game_start()
game_over()
game_restart()


# 9-9.super
# super 로 상속 받을땐 self 를 안쓴다. super().__init__(name,hp,)
# 다중 상속중 주의 할 점
class Unitadd:
    def __init__(self):
        print("Unit 생성자")


class Flyableadd:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnitadd(Unitadd, Flyableadd):
    def __init__(self):
        super().__init__()  # 다중 상속일 경우 먼저 상속받은 클래스만 호출된다
        Unitadd.__init__(self)
        Flyableadd.__init__(self)
        # 다중 상속일 경우 위와같이 class 별로 명시적으로 초기화 사용가능


# 드랍쉽
dropship = FlyableUnitadd()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


# 10-1.예외처리: 에러가 발생했을때 예외 처리할수 있다
try:  # 예외 처리는 try:로 시작해 except로 끝난다
    print("나누기 전용 계산기 입니다")
    nums = []
    # nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    # nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(10)
    nums.append(0)
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러!! 잘못된 값을 입력하였습니다")
except ZeroDivisionError as err:
    print(err)
# except:   ## 알람 메시지만 출력할수도 있다
#     print("알수 없는 에러가 발생하였습니다")
except Exception as err:  # 알수 없는 에러에 해당 에러 메세지 출력
    print("알수 없는 에러가 발생하였습니다")
    print(err)

# 10-2.에러 발생시키기
try:  # 예외 처리는 try:로 시작해 except로 끝난다
    print("한자리 숫자 나누기 전용 계산기 입니다")
    # num1 = int(input("첫 번째 숫자를 입력하세요"))
    # num2 = int(input("두 번째 숫자를 입력하세요"))
    num1 = 60
    num2 = 2
    if num1 >= 10 or num2 >= 10:
        raise ValueError  # raise를 활용해 에러를 만들수 있다
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("에러!! 잘못된 값을 입력하였습니다.num1:{0},num2:{1}".format(num1, num2))


# 10-3.사용자 정의 예외처리: 에러 코드를 만들어 사용할수있다
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __init__(self):
        pass
        # return self.msg


try:  # 예외 처리는 try:로 시작해 except로 끝난다
    print("한자리 숫자 나누기 전용 계산기 입니다")
    num3 = 60
    num5 = 2
    if num3 >= 10 or num5 >= 10:
        raise BigNumberError  # raise를 활용해 에러를 만들수 있다
    print("{0} / {1} = {2}".format(num3, num5, int(num3 / num5)))
except ValueError:
    print("에러!! 잘못된 값을 입력하였습니다.num3:{0},num5:{1}".format(num3, num5))
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요")
    print(err)

# 10-4.finally 예외 처리문중 정상이건 오류건 무조건 실행
finally:
    print("계산기를 이용해 주셔서 감사합니다")

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


# 11-1.모듈: 필요한것들을 부품처럼 만드는 것
# 모듈 불러올때는 같은 경로에 있거나 모듈들 모여있는곳에 있어야 불러 올수잇다
# 예1:
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을때 가격
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# 예2:
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# # 예3:
# from theater_module import *    # 모듈내 노든걸 사용하겟다.
# price(3)
# price_morning(4)
# price_soldier(5)

# # 예4:
# from theater_module import price, price_morning # 원하는 부분만 호출해서 사용가능
# price(3)
# price_morning(4)

# 예5:
# from theater_module import price_soldier as price   # 단일 요소만 필요 할때 별명을 붙여 간편 사용가능
# price(5)

# 11-2.패키지: 모듈 들은 모아 놓은 것
# 패키지 불러오기#1
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# 패키지 불러오기#2
trip_vo = VietnamPackage()
trip_vo.detail()

# 패키지 불러오기#3
trip_vi = vietnam.VietnamPackage()
trip_vi.detail()

# 11-3._all_ 패키지 권한을 부여할수잇다
# __init__ => __all__ = ["vietnam","thailand"]
print("# 11 - 3. _all_ ")
trip_ao = vietnam.VietnamPackage()
trip_ai = thailand.ThailandPackage()
trip_ao.detail()
trip_ai.detail()

# 11-4.모듈 직접 실행
# 패키지내 조건문을 사용해 내부에서 호출하는 건지 외부에서 호출하는건지 확인 및 테스트 가능
# if __name__ == "__main__":
#     print("VietnamPackage 모듈을 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
#     trip_to = VietnamPackage()
#     trip_to.detail()
# else:
#     print("VietnamPackage 외부에서 모듈 호출")


# 11-5.패키지, 모듈 위치  [위치 확인]
# print(inspect.getfile(random))


# 11-6.pip install
# pypi.org 추천 사이트
# pip install beautifulsoup4
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 11-7.내장함수
# 구글링: list of python builtins
# 추천 사이트:https://docs.python.org/ko/3/library/functions.html
# input:  사용자 입력을 받는 함수
# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir(random()))


# 11-8.외장함수
# 구글링:list of python modules
# 추천 사이트:https://docs.python.org/3/py-modindex.html
# glob: 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
print(glob.glob("*.py"))  # 확장자가 py인 모든 파일


# os : 운영 체제에서 제공하는 기본 기능
print(os.getcwd())  # 현재 디렉토리

# os 활용 예제
# folder = "sample_dir"
#
# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다")
#     os.rmdir(folder)    #폴더 삭제
#     print(folder,"폴더를 삭제 하였습니다.")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder,"폴더를 생성하였습니다.")

# print(os.listdir()) # 현재 폴더에 존재하는 폴더와 파일

# time: 시간 관련 함수
print(time.localtime())  # 시간 읽어 오기
print(time.strftime("%Y-%m-%d %H:%M:%S"))   # 시간 정렬 년-월-일 시:분:초

print("오늘 날짜는 ", datetime.date.today(), "입니다")

# timedalta : 두 날짜 사이의 간격
today = datetime.date.today()   # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today + td)  # 오늘 부터 100 후

print()
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 12.Outro
byme.sign()
