'''
표준입력기능의 내장함수 => input()
- 문법 : input("요청메시지")
- 결과 : 입력받는 데이터, 데이터 종류는 str
'''

# 이름을 입력받기 ==> input
name = input("이름이 뭐니? ")
x = 123
#입력 받은 데이터 출력하기 ==> print(n)
print("당신 이름은 ", name, "이군요.", sep='')
print("당신 이름은 %s이군요."%name)
print(f"당신 이름은 {name}이군요.")

# 나이 입력 받기 => input
age = input("몇 살이야?")

# 입력 받은 나이와 타입 출력 => type()
print(age, type(age)) #32 <class 'str'>, input은 모두 str

# 숫자 2개를 입력 받기 => input() 2개 사용
number1 = input("정수 1개 입력: ")
number2 = input("정수 1개 입력: ")

print(number1, type(number1))
print(number2, type(number2))

# -------------------------------------------------------------
# str ==> int 타입으로 형 변환 즉, 타입 캐스팅(Type Casting)
# - 함수 : 타입명( 데이터 )
#         str( 데이터 )   : 데이터를 str 타입으로 형 변환
#         int( 데이터 )   : 데이터를 int 타입으로 형 변환
#         float( 데이터 ) : 데이터를 float 타입으로 형 변환
#         bool( 데이터 )  : 데이터를 bool 타입으로 형 변환
# -------------------------------------------------------------

# 입력받은 정수 2개 정수로 타입 변환
int(number1)  #이 순간만 int, 저장하지 않으므로 다시 str
int(number2)
print(number1, type(number1))  #13 <class 'str'>
print(number2, type(number2))  #15 <class 'str'>

number1 = int(number1) #저장하였으므로 int로 새롭게 할당
number2 = int(number2)
print(number1, type(number1))  #13 <class 'int'>
print(number2, type(number2))  #15 <class 'int'>

# -------------------------------------------------------------
# 계산하기 => 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/)
# -------------------------------------------------------------

print(number1+number2) #합 값만 나옴

#[출력] 10 + 30 = 40 식으로 표현하고 싶음

print(f"{number1} + {number2} = {number1+number2}") #10 + 30 = 40
print(f"{number1} - {number2} = {number1-number2}") #10 - 30 = -20
print(f"{number1} * {number2} = {number1*number2}") #10 * 30 = 300
print(f"{number1} / {number2} = {number1/number2}") #10 / 30 = 0.3333333333333333

# -------------------------------------------------------------
# 계산하기 => 몫(//), 나머지(%)
# -------------------------------------------------------------

print(f"{number1} // {number2} = {number1//number2}") #10 // 30 = 0
print(f"{number1} % {number2} = {number1%number2}") #10 % 30 = 10

# -------------------------------------------------------------
# 계산하기 => 제곱(**)
# -------------------------------------------------------------

print(f"{number1} ** {number2} = {number1**number2}") #10 // 30 = 0
