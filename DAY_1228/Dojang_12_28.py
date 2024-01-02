#p.87~


#불과 비교 연산자 사용하기
print(True)
print(False)

#비교 연산자의 판단 결과
print(3>1)

#숫자가 같은지 다르지 비교하기
print(10==10)
print(10!=5)

#문자열이 같은지 다르지 비교하기
print('Python' == 'Python') #True
print('Python' == 'python') #False
print('Python' != 'python') #True

#부등호 사용하기
print(10 > 20) #False
print(10 < 20) #True
print(10 >= 10) #True
print(10 <= 10) #True

#객체가 같은지 다르지 비교하기

print(1 == 1.0)
# print(1 is 1.0)
# print(1 is not 1.0)

#정수 객체와 실수 객체가 서로 다르 것은 어떻게 확인하나요?
print(id(1))
print(id(1.0))

# #값 비교에 is를 쓰지 않기
# a = -5
# print(a is -5)
# a = -6
# a is -6
# print(a is -6)

#논리 연산자 사용하기
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(not True and False or not False)
print(((not True) and False) or (not False))

#논리 연산자와 비교 연산자를 함께 사용하기
print(10 == 10 and 10 != 5)
print(10>5 or 10<3)
print(not 10>5)
# print(not 1 is 1.0)

#정수, 실수, 문자열을 불로 만들기
print(bool(1))
print(bool(0))
print(bool(1.5))
print(bool('False'))

# 단락 평가
print(False and True) #False
print(False and False) #False
print(True or True) #True
print(True or False) #True
print(True and 'Python') #True
print('Python' and True) #False
print(False and 'Python') #False
print(0 and 'Python') #0
print(True or 'Python') #True
print('Python' or True) #'Python'
print(False or 'Python') #'Python'
print(0 or False) #False



# p.96~
hello = 'Hello, world!'
print(hello)

hello = ("안녕하세요")
print(hello)

hello = "Hello, world!"
print(hello)

hello = '''Hello, Python!'''
print(hello)
python = """Python Programming"""
print(python)

#여러 줄로 된 문자열 사용하기
hello = '''Hello, world!
안녕하세요
Python입니다.'''
print(hello)

#문자열 안에 작은따옴표나 큰따옴표 포함하기
s = "Python isn't difficult"
print(s)
s = 'He said "Python is easy"'
print(s)
# s = 'Python isn't difficult'
# s= "He said "Python is easy""

single_quote = '''"안녕하세요."
'파이썬'입니다.'''

double_quote1 = """"Hello"
'Python'"""

double_quote2 = """Hello, 'Python'"""

print(single_quote)
print(double_quote1)
print(double_quote2)

#문자열에 따옴표를 포함하는 다르 방법
print('Python isn\'t difficult') #이스케이프 문자 \'가 '의 역할

#따옴표 세 개로 묶지 않고 여러 줄로 된 문자열 사용하기
print('Hello\nPython')
print('''Hello
Python''')

#한글 문자열 출력이 안 될 때

#파이썬 셀과 스크립트 파일의 결과가 다르데요?