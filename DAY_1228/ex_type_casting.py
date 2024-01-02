"""
타입 캐스팅(Type Casting) / 형변환
- 정수 => 실수, 정수 => 문자열, 정수 => 논리
  다른데이터 타입으로 변환하는 것
- 함수
  => 정수 형변환해주는 함수 int()
  => 실수 형변환해주는 함수 float()
  => 문자열 형변환해주는 함수 str()
  => 논리 형변환해주는 함수 bool()
"""

# int 데이터 타입으로 형 변환 ---------------------------------
# int( 데이터 )
# str ==> int
# int ( 10진수 문자 '0~9')
print(type(int('200')))
value = int('200')
print(type(value))

# print(type(int('200Day'))) #10진수 써라! <= ValueError: invalid literal for int() with base 10: '200Day'
# print(type(int('200.4'))) #10진수 쓰라니까! <= ValueError: invalid literal for int() with base 10: '200.4'

# floot ==> int : 소수점 이하 데이터 손실 발생
print(type(int(200.4)), int(200.7))

# bool ==> int
# => 0, 1 => False, True
print(type(int(False)), int(False), type(False))
print(type(int(True)), int(True), type(True))
# print(type(int('True')), int('True'), type(True)) 'True'는 str


# float 데이터 타입으로 형 변환 ---------------------------------
# int( 데이터 )
# str ==> float ('0~9','.')
print(type(float('3.5')), float('3.5'))
print(type(float('35')), float('35')) #35.0이 생략된 35로 이해하고 다시 35.0으로 만듦
# print(type(float('0x123')), float('0x123')) 각 진법별 함수가 따로 있음
print(type(float('-123')), float('-123')) #-123.0

# int ==> float
print(type(float(45)), float(45)) #45.0
print(type(float(-9)), float(-9)) #-9.0

# str ==> float ('0~9','.')
