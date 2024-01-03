# 1~100 사이 2의 배수에 해당한 정수로 구성된 list--------------------------
a = list(range(2,101,2))
print(a)

# 2, 4, 6, 8, ..., 100 을 문자열로 만들려면
result = str(a)
print(result[0], result[3], result[-2], result[-1])
#str로 형변환시키면 '[', ',' ']', ' ' 도 다 들어감

print(len(result)) # 197
# int ==> str 형변환
# result[0] = str(result[0]) 를 197회 반복해야..

# --------------------------------------------------------
# 시퀀스 데이터 타입에서 원소/요소를 하나씩 빼서 반복 코드 수행 => for in 반복문
# --------------------------------------------------------

# for문 안에 넣으면 계속 반복해서 덮어씌워짐
strNum = ''
for num in result:
    strNum = strNum + str(num)
print(f'str(num) => {type(strNum)}\n{strNum}')

# --------------------------------------------------------
# list 안에 모든 원소를 str 타입으로 변환해서 저장
# --------------------------------------------------------
# num[인덱스] = str(num[인덱스])
# 데이터의 인덱스 범위 => 0 ~ len(data)-1
print(range(len(a)))

print(f'[BEFORE] a => {a}')

for idx in range(len(a)):
    a[idx] = str(a[idx])
print(f'[AFTER] a => {a}')