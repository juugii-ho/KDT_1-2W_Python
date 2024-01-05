# -----------------------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# -----------------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
#           팩토리얼이란? 3! = 3 * 2* 1
# 함수 이름 : factorial
# 매개 변수 : a,b,c,d,e
# 반 환 값 : 팩토리얼 결과
# -----------------------------------------------------------------

def factorial(number):
    numbers = 1
    for number in range(1, number+1):
        numbers = numbers * number
    value = numbers
    return value

print(factorial(3))

# 내가 만든 것
# -----------------------------------------------------------------
# 선생님이 만든 것

def factorial2(x):
    ret = 1
    if x:
        for n in range(x, 0, -1): ret *= n      # ret = ret *n
    return ret

print(factorial2(3))
# -----------------------------------------------------------------
# 다르게 제시하는 법
#
# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 아래와 같은 형태로 반환해 주는 기능
#           예시 결과 3! = 3 * 2 * 1 = 6
# 함수 이름 : factorial3
# 매개 변수 : x
# 반 환 값 : 팩토리얼 결과
# -----------------------------------------------------------------
def factorial3(x):
    ret = 1
    if x:
        for n in range(x, 0, -1): ret *= n
    strRet = ''
    for n in range(x, 0, -1):
        strRet = strRet + str(n) + (" * " if n != 1 else " = ")
    return str(x) + "! = " + strRet + str(ret)

print(factorial3(0))



