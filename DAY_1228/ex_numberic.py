# '''
# 논리 연산자 => and, or, not
# - 결과 : True, False
# - 동작방식
#     * and => A and B : A, B 모두 True일 때만 True
#     * or  => A or B  : A, B 중 하나 이상 True가 되면 True
#     * not =>  not A  : 현재 A의 상태를 반대로 True <=> False
#                         not True = False
#                         not False = True  반대로 만들어주는 토글 toggle
# '''
#
# no1 = 10
# no2 = 3
# # no1, no2 = 10, 3
#
# # and 연산자----------------------------------------------
# # no1은 no2보다 크다 그리고 100보다 큰 수
# print( no1 > no2 , no1>100 ) #True False
# print( no1>no2 and no1>100 ) #False
# print( no1>no2 and no1>100 and no1>0) #False
#
# # or 연산자----------------------------------------------
# # 1개 이상만 True가 되면 True로 결정
# print( no1 > no2 , no1>100 ) #True False
# print( no1>no2 or no1>100 ) #False
# print( no1>no2 or no1>100 and no1>0) #False
#
# # not 연산자----------------------------------------------
# # 현재 값을 반대로 즉, True => False, False => True
# # False => 0, True => 1 / 0이 아닌 모든 숫자
# print(not False, not True)
# print(not 0, not 1)
# print(not 2, not -3, not 0.0)
#
#
# '''
# 객체 비교 연산자 => is, is not
# - 결과 : True, False
# - 동작방식
#     * is => A is B : A, B가 동일한 데이터 타입의 객체 여부
#     * is not  => A is not B  : A, B가 서로 다르 데이터 타입의 객체 여부
# '''
# print(f'10 is 10 => {10 is 10}')
# print(f'10 is 21 => {10 is 21}')
# print(f'10 is 20.0 => {10 is 10.0}')
#
# print(f'10 is 10 => {10 == 10}')
# print(f'10 is 21 => {10 == 21}')
# print(f'10 is 20.0 => {10 == 10.0}')




# -------------------------------------------------------------
# [실습1] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술 연산 결과를 출력하세요.
#        +, -, *, /, //, %, **
#        [출력 예시] 10 + 4 = 14
# -------------------------------------------------------------

# -------------------------------------------------------------
# [실습2] [실습1]에서 입력 받은 숫자 데이터를 활용하여 비교 연산 결과를 출력하세요.
#        >, <, >=, <=, ==, !=
#        [출력 예시] 10>4   => True
#                  10==4  => False
# -------------------------------------------------------------

# -------------------------------------------------------------
# [실습3] [실습1]에서 입력 받은 숫자 데이터를 활용하여
#        최댓값과 최솟값을 추가로 입력 받은 후 논리연산 결과를 출력하세요.
#        [출력 예시] 10>4 and 10>최대값 => True
#                  not 10           => False
#
# -------------------------------------------------------------


number1 = int(input('첫 번째 숫자 데이터를 입력하세요: '))
number2 = int(input('두 번째 숫자 데이터를 입력하세요: '))

print(f'{number1} + {number2} = {number1+number2}')
print(f'{number1} - {number2} = {number1-number2}')
print(f'{number1} * {number2} = {number1*number2}')
print(f'{number1} / {number2} = {number1/number2}')
print(f'{number1} // {number2} = {number1//number2}')
print(f'{number1} % {number2} = {number1%number2}')
print(f'{number1} ** {number2} = {number1**number2}')

print(f'{number1} > {number2} => {bool(number1>number2)}')
print(f'{number1} < {number2} => {bool(number1<number2)}')
print(f'{number1} >= {number2} => {bool(number1>=number2)}')
print(f'{number1} <= {number2} => {bool(number1<=number2)}')
print(f'{number1} == {number2} => {bool(number1==number2)}')
print(f'{number1} != {number2} => {bool(number1!=number2)}')

max_number = int(input('임의의 최댓값 데이터를 입력하세요: '))
min_number = int(input('임의의 최솟값 데이터를 입력하세요: '))

print(f'{number1} > {number2} and {number1} > {max_number} => {number1>number2 and number1>max_number}')
print(f'{number1} > {number2} and {number1} > {min_number} => {number1>number2 and number1>min_number}')
print(f'not {number1}  => {bool(not number1)}')

print(f'{number1} > {number2} or {number1} > {max_number} => {number1>number2 or number1>max_number}')
print(f'{number1} > {number2} or {number1} > {min_number} => {number1>number2 or number1>min_number}')
print(f'not {number1}  => {bool(not number1)}')


# -------------------------------------------------------------

# 입력 => str 데이터 타입

no1 = input("숫자 입력 : ")
no2 = input("숫자 입력 : ")

# str => int : 타입 캐스팅
no1 = int(no1)
no2 = int(no2)

#산술 연산 출력
print(f' {no1} + {no2} = {no1+no2}')

#비교 연산 출력


#str 문자 타입
maxValue=input("임의의 큰 수 입력 : ")
minValue=input("임의의 작은 수 입력 : ")

#str => int 변환
maxValue = int(maxValue)
minValue = int(minValue)

#논리 연산 결과 출력
#and 연산자 => 왼쪽/오르쪽 모두 True인 경우만 True
print(f"{no1}>{no2} and {no1} > {maxValue} => {no1>no2 and no1>maxValue}")
print(f"{no1}>{no2} and {no1} > {minValue} => {no1>no2 and no1>minValue}")

#or 연산자 => 왼쪽/오르쪽 모두 False인 경우만 False가 됨
print(f"{no1}>{no2} or {no1} > {maxValue} => {no1>no2 or no1>maxValue}")
print(f"{no1}>{no2} or {no1} > {minValue} => {no1>no2 or no1>minValue}")

# not 연산자 => not 데이터, not 변수명
print(f'not {no1} => {not no1}')


