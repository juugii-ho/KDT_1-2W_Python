# --------------------------------------------------------
# for 요소 in 시퀀스/반복가능한 객체:
# ==> for 인덱스 in range(len(변수)):
# ==> 내장함수 enumerate()
# - (번호, 요소) 묶음으로 반환 함!!
# --------------------------------------------------------
datas = ['Apple', 'Banana', 'Orange']

# 리스트 안에 요소/원소 데이터 추출
for data in datas:
    print(data)

# 리스트 안에 요소/원소 (인덱스,데이터) 추출
for data in enumerate(datas):
    print(data)  # (0, 'Apple') \n (1, 'Banana') \n (2, 'Orange')

for data in enumerate(datas, start=100):
    print(data)  # (100, 'Apple') \n (101, 'Banana') \n (102, 'Orange')

# --------------------------------------------------------

x = ['std01', 'std02', 'std03']
y = [100, 200, 300]

# for 방법
myDict = {}
for data in enumerate(x):
    myDict[data[1]] = y[data[0]]
print(myDict)

# 언패킹방식 방법2
myDict = {}
for idx, key in enumerate(x):
    myDict[key] = y[idx]
print(myDict)

# enumerate 방법
for data in enumerate(x):
    print(data, end=', ')   #(0, 'std01'), (1, 'std02'), (2, 'std03'),

