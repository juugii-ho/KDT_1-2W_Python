# 주석 comment => 인터프리터가 해석하지 않는 코드
# 코드에 설명을 작성 하는 용도 => 필수!!
print("Hello~")

# 시키고 싶은 일 : 숫자, 글자 데이터를 화면에 출력하기
# 출력하기 ==> print(데이터)
# 숫자 데이터 출력 => 정수 int
print(2024)
#print(1227) print(33) SyntaxError: invalid syntax - 문법 에러 : 유효하지 않은 문법
print(1227)
print(33)
#한 줄에 하나씩 쓰는 것이 기본 원칙
print(1000)

# 숫자 데이터 출력 => 실수 float
print(2.9)
print(5.123)
print(1.) #'.'이 붙어서 실수가 됨. 0이 생략된 실수 형태이므로 1.0으로 표기

# 문자/글자/문자열 데이터 출력 => 글자 str
# '데이터', "데이터"
# print(홍길동) NameError: name '홍길동' is not defined
print('홍길동') #홍길동
print("'홍길동'") #'홍길동'
# print(""홍길동"") SyntaxError: invalid syntax
print('"홍길동"') #"홍길동"
# print(''홍길동'') SyntaxError: invalid syntax
print("Happy New Year")
print('2024.') #2024는 정수, 2024.은 실수 '2024.'는 문자열

#'''데이터'''', """데이터""" : 여러줄 문자열
print('''Good
Luck
Happy''') #여러줄 문자는 ''' 이용, 주석에도 이용되지만 데이터에 들어가면 용도 바뀜
print('''Good
         Luck
         Happy''') # Luck, Happy 앞의 공백까지 표기되므로 위와 같이 해야
#print('Good
#       Luck
#       Happy') 홑따옴표 하나만 있을 때는 에러남
print("""Good
        Luck
        Happy""") #Good /      Luck /     Happy 식으로 표기됨
