# -----------------------------------------------------------------
# 모듈(Module) : 특정 목적의 변수, 함수, 클래스를 하나의 파일에 담은 것
# - 예 : 수학 관련 변수, 함수, 클래스 ==> math.py
#        파이썬 기본 제공 변수, 함수, 클래스 ==> builtin.py
# - 사용법 : import 모듈명
# - 모듈의 기능 사용법 : 모듈명.변수명
#                    모듈명.함수명()
# -----------------------------------------------------------------
# 사용하고 싶은 변수, 함수, 클래스가 있는 모듈 포함

import random       # 임의의 수를 추출해주는 변수, 함수, 클래스 있는 모듈
import math         # 수학 관련 변수, 함수, 클래스 있는 모듈

# 모듈 안에 있는 변수, 함수, 클래스 사용
print(math.pi)

print(math.factorial(5))

# 팩토리얼 만들어보기
num = int(input("몇 팩토리얼을 구할까요?"))
data1 = 1
for data in range(1,num+1):
    data1 = data1*data
print(data1)

# 임의의 0.0 <= ~ < 1.0 사이의 임의의 실수 추출 => random() 함수
# for cnt in range(10):
#     print(random.random())

# 임의의 0 <= ~ < 10 사이의 임의의 정수 추출 => random() 함수
# for cnt in range(10):
#     print(int(random.random() * 10))

# 임의의 1 <= ~ <= 10 사이의 임의의 정수 추출 => random() 함수
# for cnt in range(10):
#     print(int(random.random() * 10)+1)

# a <= ~ <= b 사이의 임의의 정수 추출 => randint() 함수
for cnt in range(10):
    print(random.randint(1,10), end=' ')
print()


myLotto = []
END_POINT = 6
while True:
    if len(myLotto) == END_POINT: break
    num = random.randint(1,45)
    if num not in myLotto:
        myLotto.append(num)

print(sorted(myLotto))


myLotto = set()
END_POINT = 6
while True:
    if len(myLotto) == END_POINT: break
    num = random.randint(1,45)
    myLotto.add(num)

print(sorted(myLotto))