# -----------------------------------------------------------------
# 다양한 함수의 형태 - (2) 반환값 없는 함수
# -----------------------------------------------------------------
# 함수 기능 : 2개의 정수를 덧셈 후 출력해주는 기능
# 함수 이름 : addTwo
# 매개 변수 : x, y
# 반 환 값 : 없음
# -----------------------------------------------------------------

def addTwo(x,y):
    value = x+y
    print(f'{x}+{y}={value}')

# 함수 사용, 즉 함수 호출 ----------------------------------------------
addTwo (10,3)

# 반환값이 없는 함수들
# [].sort()
# [].pop()

# 함수 호출 시에 매개변수 갯수와 동일하게 데이터 전달해야 함!! ------------------
# ERROR
# addTwo(10,10,10)
# addTwo(10)
# -----------------------------------------------------------------

# -----------------------------------------------------------------
# 함수 기능 : 영어 단어를 입력 받아서 모두 대문자로 변환 해주는 기능
# 함수 이름 : convertCase
# 매개 변수 : word
# 반 환 값 : 없음
# -----------------------------------------------------------------
def convertCase(word):
    word = word.upper()
    return word
# -----------------------------------------------------------------
# 함수 기능 : 시퀀스 객체의 모든 원소를 대문자로 변환 해주는 기능
# 함수 이름 : convertCase2
# 매개 변수 : str 타입의 원소로 구성된 list
# 반 환 값 : 없음
# -----------------------------------------------------------------

def convertCase2(dataList):
    for idx in range(len(dataList)):
        dataList[idx] = dataList[idx].upper()


dataList = [('apple'), ('danger')]
for idx, data in enumerate(dataList):
    dataList[idx] = data.upper()
print(dataList)

# 함수 사용 즉, 함수 호출 ----------------------------------------------
datas = ['Apple', 'Banana', 'Mango']
print(f'[Before]{datas}')

dconvertCase2(datas)

print(f'[After] {datas}')

# ㄴ 이미 값이 다 바뀌었기 때문에 return 값이 필요없는 경우
# 하지만 필요하다면 아래와 같이 수정하면 됨

def convertCase2(dataList):
    for idx in range(len(dataList)):
        dataList[idx] = dataList[idx].upper()

def convertCase(word):
    word = word.upper()
    return word

datas = ['Apple', 'Banana', 'Mango']
print(f'[Before]{datas}')

# convertCase2(datas)
datas[0]=convertCase(datas[0])

print(f'[After] {datas}')