'''
수치 데이터 살펴보기
- 정수 => class int       : 양수, 0, 음수
- 실수 => class float     : 소수점 존재
- 복소수 => class complex
'''
# ----------------------------------------------------------
# [실습] 2개의 정수를 입력받기
# -> input() 함수 2개 사용
# -> str => int 타입 캐스팅
# ----------------------------------------------------------

# [방법1]
# number1 = int(input("첫 번째 정수를 입력해주세요: "))
# number2 = int(input("두 번째 정수를 입력해주세요: "))

# [방법2]
number1 = input("첫 번째 정수를 입력해주세요: ")
number2 = input("두 번째 정수를 입력해주세요: ")
number1 = int(number1)
number2 = int(number2)

# ----------------------------------------------------------
# 비교 연산 결과 출력
# [ 출력 ] 10>3 => True
print("%d>%d => %s" %(number1, number2, number1>number2))
# print(f"{number1}>{number2} => {number1>number2}")

print("%d<%d => %s" %(number1, number2, number1<number2))

print("%d>=%d => %s" %(number1, number2, number1>=number2))

print("%d<=%d => %s" %(number1, number2, number1<=number2))

print("%d==%d => %s" %(number1, number2, number1==number2))

print("%d!=%d => %s" %(number1, number2, number1!=number2))


# ----------------------------------------------------------
