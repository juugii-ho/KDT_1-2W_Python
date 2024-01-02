# ---------------------------------------------------------------
# dict 데이터 전용 함수 즉 메서드(Method)
# ---------------------------------------------------------------
# 빈 dict----------------------------------------------------
myDict = {}

# 데이터 추가 => myDict[키]=데이터--------------------------
myDict['one']=100

# 데이터 추가 => update() 메서드--------------------------
# myDict.update('two', 200) TypeError: update expected at most 1 argument, got 2
# myDict.update(('two', 200)) TypeError: update expected at most 1 argument, got 2

# 데이터 추가 => myDict[키]=데이터--------------------------
# 주의!!! 키는 str 타입만 가능, str 타입이지만 '', "" 사용 안 됨
myDict.update(two = 200)    # 여기서 two는 매개변수이므로 변수명이라 '' 쓰면 안 됨
                            # 매개변수는 변수명 짓기 위한 변수 - 글로 보니 더 헷갈림..
print(f'myDict : {myDict}')
# myDict.update(2= 200)     # 변수명은 여기서도 숫자로 시작할 수 없음
myDict.update(two = 300, _1 = 1000)
print(f'myDict : {myDict}')

# 키만 추출해서 읽어오는 메서드 => keys() 메서드 --------------------------
keys = myDict.keys() # 뷰 타입을 제공
print(f'myDict의 키들 : {keys}, {type(keys)}')
# myDict의 키들 : dict_keys(['one', 'two', '_1']), <class 'dict_keys'>
# 메모리 문제로 새로운 객체를 만드는 게 아니라 기존 데이터를 활용해 미리보기(view)를 시켜주는 것

# 값만 추출해서 읽어오는 메서드 => values() 메서드 --------------------------
values = myDict.values() # 뷰 타입을 제공
print(f'myDict의 밸류들 : {values}, {type(values)}')


# 키와 값을 묶은 아이템을 추출해서 읽어오는 메서드 => items() 메서드 --------------------------
# (키, 값) 튜플 형식으로 묶어서
items = myDict.items() # 뷰 타입을 제공
print(f'myDict의 키/값 묶음들 : {items}, {type(items)}')

# 딕셔너리는 인덱스가 없기 때문에 keys, values, items는 아주 많이 사용

myDict2 = { 1 : 2, 3 : 4}
keys2 = myDict2.keys()
print(f'myDict2의 키들 : {keys2}, {type(keys2)}')
#  myDict2의 키들 : dict_keys([1, 3]), <class 'dict_keys'>

# 원소/요소 단위 접근 위해서는 형변환 필요함!!
items = list(myDict.items())
print(f'myDict의 키/값 묶음들 : {items[0]}, {type(items)}')

# 원소/요소 모두 삭제해주는 메서드 => clear() 메서드
# del myDict의 경우 키마다 삭제해줘야해서
# myDict.clear()
# print(f'myDict : {myDict}, {len(myDict)}개') # {} 빈 딕셔너리가 됨


# 원소/요소 데이터 읽기 메서드 => 변수명[키] ==> 값, get(키) 메서드
print(f'myDict.get("one") : {myDict.get("one")}, {(myDict["one"])}개') # {} 빈 딕셔너리가 됨
print(f'myDict.get("three") : {myDict.get("three")}') # None으로 반환
# print(f'myDict.["three"] : {myDict.["three"]}')       # 에러남

# 원소/요소 데이터 읽기 메서드 => 변수명[키] ==. 값, get(키, 기본값) 메서드
# => 키가 존재하지 않으면 기본값 반환
print(f'myDict.get("three", 0) : {myDict.get("three", 0)}') # None으로 반환
print(f'myDict.get("three", "존재 하지 않음") : {myDict.get("three", "존재 하지 않음")}') # None으로 반환



# ---------------------------------------------------------------
# 멤버 연산자 => 원소 in 여러개 저장 타입
#          => 원소 not in 여러개 저장 타입
# - 여러개 저장 타입 : str, list, tuple, dict, set
# - 연산 결과 => True / False
# ---------------------------------------------------------------
aList = [1, 2, 3]
aTuple = 11, 22
aDict = {1 : 100, 2 : 100}

print(f'''1 in aList : {1 in aList}    
1 in aTuple : {1 in aTuple}
1 in aDict : {1 in aDict}
1 in aDict : {100 in aDict}''')
# True False True False(Dict는 키 존재여부만 봄)
# 딕셔너리의 값, 아이템 형식의 리스트/튜플을 넣어도 False 나옴