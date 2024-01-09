# ----------------------------------------------------------
# filter(함수명, 반복가능객체)
# - 조건에 맞는 데이터만 반환
# ----------------------------------------------------------
# 예) 5초과 10미만 데이터만 추출
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

# filter()

# def check(data):
#     return data>5 and data<10   # 연산의 결과는 True / False
#
# a = list(filter(check, a))      # filter는 True일 때만 출력
# print(a)


# import random                           # random.py 파일의 모든 변수, 함수, 클래스 가져오기
# from random import randint, random     # random.py 파일에서 randint,random 함수만 가져오기
#
# print(randint(1,10))
# print`(random())
from functools import reduce


def f(x,y):
    return x+y

print(reduce(f,a))

print(reduce(lambda x, y: x+y, a))