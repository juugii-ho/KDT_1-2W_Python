# ----------------------------------------------------------
# 참조형 변수 => 데이터의 주소 저장
# ----------------------------------------------------------
# 저장된 데이터 & 변수 타입 관계-----------------------------------

num = 12 # num에는 12가 아닌 12의 주소값이 저장됨
print(f'num => {id(num), type(num)}')

num = 3
print(f'num => {id(num), type(num)}')

num ="Good"
print(f'num => {id(num), type(num)}')

num1 = []
print(f'num1 => {id(num1), type(num1)}')

num2 = [11, 22.1]
print(f'num2 => {id(num2), type(num2)}')
print(f'num[0] => {id(num2[0]), type(num2[0])}')
print(f'num[1] => {id(num2[1]), type(num2[1])}')

print("==================== 값 변경 ====================")
num = "Happy"
print(f'num => {id(num), type(num)}')

num2[0]=100
print(f'num2 => {id(num2), type(num2)}') # num2[0]가 바뀌어도 num의 리스트라는 바구니는 바뀌지 않기 때문에 id(num2) 주소값 유지됨
print(f'num2[0] => {id(num2[0]), type(num2[0])}')

num2 = num1
print(f'num2 => {num2, id(num2), type(num2)}')
print(f'num1 => {num1, id(num1), type(num1)}')
# 위의 num1 주소값을 num2에 입힌것
