# p.50~

print('Hello, world!')
print('Python Programming')

print('Hello'); print('1234')

# Hello, world! 출력
print('Hello, world!')

a = 1 + 2 # 더하기
print('Hello, world!') #print('1234567890')

#print('Hello, world')
#print('12345667890')

# 더하기
# a = 1 + 2
print('Hello, world!')

# if a == 10:
# print('10입니다.') # IndentationError: expected an indented block

if a == 10:
    print('10입니다.')    #들여쓰기 공백은 4칸

if a == 10:
    print('10')
    print('입니다.')


#p.55~
#프롬프트에서 해보기
#사칙연산
# >>> 1+1
print(1+1)
# >>> 1-2
print(1-2)
# >>> 2*2
print(2*2)
# >>> 5/2
print(5/2)
# >>> 4/2
print(4/2)
#
# #몫 구하기
# >>> 5//2
print(5//2)
# >>> 4//2
print(4//2)
# >>> 5.5//2
print(5.5//2)
# >>> 4//2.0
print(4//2.0)
# >>> 4.1//2.1
print(4.1//2.1)
#
# #나머지 구하기
# >>> 5 % 2
print(5%2)
#
# #거듭제곱 구하기
# >>> 2 ** 10
print(2**10)

#값을 정수로 만들기
#int(3.3)
print(int(3.3))
#int(5/2)
print(int(5/2))
#int('10')
print(int('10'))

#몫과 나머지 함게 구하기
print(divmod(5,2)) #(2,1)
quotient, remainder = divmod(5,2)
print(quotient, remainder) #2 1

#2진수'0b', 8진수'0o', 16진수'0x' or '0X'
print(0b110) #6
print(0o10) #8
print(0xF) #15

#객체의 자료형 알아내기
print(type(10)) #<class 'int'>

#실수 계산하기
print(3.5 + 2.1) #5.6
print(4.3 - 2.7) #1.5999999999999996 실숫값의 오차로 반올림
print(1.5 * 3.1) #4.65
print(5.5 / 3.1) #1.7741935483870968

#실수와 정수를 함께 계산하면? - 표현 범위가 넓은 쪽으로 계산됨
print(4.2 + 5) #9.2

#값을 실수로 사용하기
print(float(5)) #숫자 5.0
print(float(1 + 2)) #계산식 3.0
print(float('5.3')) #문자열 5.3
print(type(3.5)) #<class 'float'>

#복소수 - 뒤에 j 붙여서
print( 1.2 + 1.3j) #(1.2+1.3j)
print(complex(1.2, 1.3)) #(1.2+1.3j)

#괄호 사용하기 - 곱셈, 나눗셈 먼저
print(35 + 1 * 2) #37
print((35 + 1) * 2) #72


# p.63 ~

# 변수 만들기
x = 10
print(x) #10

y = 'Hello, world!'
print(y) #Hello, world!
# "=" 기호는 오른 쪽 값을 변수에 할당한다는 의미, 실제 "="는 "=="로 표기

# 변수의 자료형 알아내기
print(type(x)) #<class 'int'>
print(type(y)) #<class 'str'>

x, y, z = 10, 20, 30
print(x) #10
print(y) #20
print(z) #30

# x, y, z = 10, 20
# print(x) #10
# print(y) #20
# print(z) #ValueError: not enough values to unpack (expected 3, got 2) - 값이 3개 필요한데 2개만 주어짐

x = y = z = 10
print(x) #10
print(y) #10
print(z) #10

x, y = 10, 20
x, y = y, x #x=10, y=20 값이 x=20, y=10으로 새로 할당됨
print(x) #20
print(y) #10

#변수 삭제하기
x = 10
del x
# print(x) NameError: name 'x' is not defined 변수 x가 정의되지 않음

#빈 변수 만들기
x = None
print(x) #None 다른 언어에서의 Null

#변수로 계산하기
a = 10
b = 20
c = a + b
print(c) #30

a = 10
print(a + 20) #30
print(a) #10

a = 10
a = a + 20
print(a)

a = 10
a += 20
print(a)

#d += 10 NameError: name 'd' is not defined 변수 d가 정의되지 않음

#부호 붙이기
x = -10
print(+x) #-10
print(-x) #10

#입력 값을 변수에 저장하기
#input() "Hello World!" 입력

#x = input()
#print(x) 입력한 값이 그대로 출력

# x = input('문자열을 입력하세요: ')
# print(x)

# 두 숫자의 합 구하기
# a = input('첫 번째 숫자를 입력하세요: ') #10
# b = input('두 번째 숫자를 입력하세요: ') #20
# print(a+b) #1020

# # 입력 값을 정수로 변환하기
# a = int(input('첫 번째 숫자를 입력하세요: ')) #10
# b = int(input('두 번째 숫자를 입력하세요: ')) #20
# print(a+b) #30

#입력 값을 변수 두 개에 저장하기
# a, b = input('문자열 두개를 입력하세요: ').split()
# Hello Python 입력
# print(a) Hello
# print(b) Python

# a,b = input('숫자 두 개를 입력하세요: ').split() #10 20
# print(a + b) #1020

# a, b = input('숫자 두 개를 입력하세요: ').split()
# a = int(a) #10
# b = int(b) #20
# print(a+b) #30
# print(int(a) + int(b)) #30

# a,b = map(int, input('숫자 두 개를 입력하세요: ').split()) #10 20
# print(a+b) #30

# a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) #10,20
# print(a+b) #30

#값을 여러 개 출력하기
print(1,2,3)
print('Hello', 'Python')
print(1, 2, 3, sep=', ')
print(4, 5, 6, sep=', ')
print('Hello', 'Python', sep='')
print(1920, 1080, sep='x')

#줄바꿈 활용하기
print(1, 2, 3)
print(1, 2, 3, sep='\n')
print('1\n2\n3')

#end 사용하기
print(1) # 1
print(2) # 2
print(3) # 3

print(1, end='')
print(2, end='')
print(3) #123

#불과 비교 연산자 사용하기
True
False

#비교 연산자의 판단 결과
print(3>1) #True

# 숫자가 같은지 다른지 비교하기
print( 10 == 10) #True
print( 10 != 5)  #True

#문자열이 같은지 다르지 비교하기
print('Python' == 'Python') #True
print('Python' == 'python') #False
print('Python' != 'python') #True

#부등호 사용하기
print(10 > 20) #False
print(10 < 20) #True
print(10 >= 10) #True
print(10 <= 10) #True
