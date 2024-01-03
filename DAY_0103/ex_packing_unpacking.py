# --------------------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
msg = "Happy New Year"
msgList = msg.split()
# Happy, Year만 가져오고 싶다면?

# 팩킹(Packing) 방식 - 덩어리 째로 변수 유지
print(msgList[0], msgList[-1])

# 언팩킹(Unpacking) 방식 - 각자 새로운 변수로 저장
# 데이터 수와 변수 수가 동일해야 함!!
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 데이터와 변수 수가 달라서 Error 발생
# 값이 3개인데 변수를 2개만 지정하면 작동하지 않음
# m1, m2 = msg.split()
# print(m1, m2) #ValueError: too many values to unpack (expected 2)

# 변수를 여러 개 생성하는 경우---------------------------------
age = 12
name = "Hong"
job = ("학생")

# 튜플을 언팩킹하여서 생성 가능
age1, name1, job1 = 12, 'Hong', '학생'   # 좌변 언팩킹, 우변 튜플의 양식을 이용한 것
info = (12, 'Hong', '학생')              # 튜플 기본 입력 방식

print(age1, name1, job1)
print(info)

# ------------------------------------------------------------------
# # 과제에서의 예시
# # key와 value로 데이터 분리했을 때
# datas = twoData.split(',')         # aa bb cc dd, 1.1 2.2 3.3 4.4
# keys = datas[0].split()            # aa bb cc dd
# values = datas[1].split()          # 1.1 2.2 3.3 4.4
#
# #언팩킹 이용하면
# keys, values = twoData.split(',')  #으로 축약해서 가능
# # ------------------------------------------------------------------



#어디서 쓰는걸까?
def myFunc(a, b):
    return a+b, a-b, a*b, a/b if not b else -1

result = myFunc(10, 3)
print(f'덧셈 결과 : {result[0]}, 뺄셈 결과 : {result[1]}, 곱셈 결과 : {result[2]}, 나눗셈 결과 : {result[3]}')

plus, minus, multi, div = myFunc(10,3)
print(f'덧셈 결과 : {plus}, 뺄셈 결과 : {minu}, 곱셈 결과 : {multi}, 나눗셈 결과 : {div}')
# 로 쓰면 가독성도 높아지고 편해짐