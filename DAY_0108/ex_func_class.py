# ----------------------------------------------------------
# 함수와 클래스
# ----------------------------------------------------------

# 변수에 어떤 데이터를 저장하고 있는 지 확인 함수 => type(변수명)
data=1
print(f'data Type => {type(data)}')

data='Good'
print(f'data Type => {type(data)}')

# 함수명 의 타입
print(f'id().Type => {type(id)}') #id().Type => <class 'builtin_function_or_method'>

# 함수 - 내장함수
#     ㄴ 사용자 정의 함수

# 사용자 정의 함수 생성 ----------------------------------------------------------
# 함수 기능 : 2개 정수 더한 후 결과 출력 기능
# 함수 이름: addTwo
# 매개 변수 : n1, n2
# 반환 결과 : 없음
# ----------------------------------------------------------
def addTwo(n1, n2):
    print( n1 + n2 )

# addTwo(3,4)

# 함수의 타입 출력 ===> type() 내장함수 사용 => class function
print( type ( addTwo))      # <class 'function'>
# addTwo. 가능

# ----------------------------------------------------------
# 함수와 변수
# - 함수명은 코드의 시작 주소를 저장하고 있음
# - 함수명을 변수에 대입 가능
# ----------------------------------------------------------
test = addTwo
print(f'test => {id(test)}, {type(test)}')       # test => 4372930912, <class 'function'>
print(f'addTwo => {id(addTwo)}, {type(addTwo)}') # addTwo => 4372930912, <class 'function'>

test(10,20)
addTwo(5,1)

# ----------------------------------------------------------
# [활용예]
# - 1~10 범위에서 임의의 정수 5개를 저장
# - 중복된 정수 저장 가능
# ----------------------------------------------------------
import random
ranList = []
for i in range(1,6):
    ranNum = random.randint(1,10)
    ranList.append(ranNum)
print(ranList)
# 내가 한 것
# ----------------------------------------------------------
# 선생님 버전
import random
nums=[]
for count in range(5):
    nums.append(random.randint(1,10))
# ----------------------------------------------------------
# 5개의 정수에서 최대값, 최소값, 내림차순 정렬된 값 출력
print(f'최댓값 : {max(nums)}')
print(f'최솟값 : {min(nums)}')
print(f'정 렬 : {sorted(nums, reverse=True)}')
print(f'합 계 : {sum(nums)}')
print(f'갯 수 : {len(nums)}')

# 여러 개의 함수 이름을 변수에 저장 => 리스트 사용함
funs = [max, min, sorted, sum, len]
for f in funs:
    if f==sorted:
        print(f(nums, reverse=True))
    else:
        print(f(nums))

# data = []
# datas = ["3", 'abc', 'Good', "72"]
# for d in datas:
#     if d.isdecimal():
#         data.append(d)
# print(data)                                   # 이것과 같은 방식 함수라고 다를 것 없음

funDict = { '최댓값': max, '최솟값' : min, '정 렬': sorted, '합 계': sum, '갯 수': len}
for k, v in funDict.items():                    # 언패킹해서 만드는 건 아직 머리에 떠오르지조차 않는다.ㅠㅠ
    if v==sorted:
        print(f'{k} : {v(nums, reverse=True)}')
    else:
        print(f'{k} : {v(nums)}')

# 사용자
