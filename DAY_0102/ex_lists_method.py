# ---------------------------------------------------------
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(Method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호침
# - 사용법 : 데이터, 메서드명() 또는 변수명,메서드명()
# ---------------------------------------------------------
# List 전용 메서드 살펴보기
# [1] 리스트에 데이터 추가해주는 메서드 => append() 맨 끝에 원소로 추가
import numpy

nums=[]

print(f'{len(nums)}개')

nums.append(10)
nums.append('One')
nums.append(True)
print(f'nums : {len(nums)}개, {nums}') #nums : 3개, [10, 'One', True]

# [1] 리스트에 데이터 추가해주는 메서드 => inser(위치인덱스, 데이터) 지정위치에 추가

nums.insert(0, 2024)
print(f'nums : {len(nums)}개, {nums}') # nums : 4개, [2024, 10, 'One', True]

nums.insert(-1,["ABC", "DEF"])
print(f'nums : {len(nums)}개, {nums}') # nums : 5개, [2024, 10, 'One', ['ABC', 'DEF'], True]

del nums[-2][-1]
print(f'nums : {len(nums)}개, {nums}') # nums : 5개, [2024, 10, 'One', ['ABC'], True]

# 리스트 아에 모드 워소 삭제해서 빈 리스트를 만들어주세요
del nums[:]
print(f'nums : {len(nums)}개, {nums}')


# [2] 리스트 안에 원소/요소 정렬해주는 메서드 => sort() 오름차순 정렬
# - 오름차순 : 작은 데이터부터 큰 데이터 순으로 정렬
nums.append(98)
nums.append(-2)
nums.append(4)
nums.append(0)
nums.append(0.1)

nums.sort()
print(f'nums : {len(nums)}개, {nums}')
#nums = nums.sort() None 이기 때문에 저장해도 안됨


# - 내림차순 : 큰 데이터부터 작은 데이터 순으로 정렬
nums.sort(reverse=True)
print(f'nums : {len(nums)}개, {nums}')

# [3] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어 주는 메서드 => reverse()
# 원소/요소 데이터 값 비교 안 함!! 순서만 변경함!
nums.reverse() # 반환값 None이기 때문에 저장해도 안됨
print(f'nums : {len(nums)}개, {nums}')


# [4] 리스트 안에 특정 원소/요소 삭제해주는 메서드 => remove()
# - 리스트에서 지정된 값의 원소 삭제
# - 없는 값/데이터 삭제 요청 시 Error 발생시킴!!
nums.remove(0) # 인덱스가 아니라 해당 값으로 삭제함, 반환값 None
print(f'nums : {len(nums)}개, {nums}')

# nums.remove(0) #없는 값 지워보기
# print(f'nums : {len(nums)}개, {nums}') ValueError: list.remove(x): x not in list


# [5] 리스트 안에 모든 원소/요소 삭제해주는 메서드 => clear()
nums.clear()
print(f'nums : {len(nums)}개, {nums}')

# nums[0] = 'A'

# [6] 리스트 안에 원소/요소 꺼내는 메서드 => pop()

nums.append(10)
nums.append(True)
nums.append(7)
print(f'nums : {len(nums)}개, {nums}')

nums.pop()
print(f'nums : {len(nums)}개, {nums}')

# [6] 리스트 안에 원소/요소 꺼내는 메서드 => pop(인덱스)
a = nums.pop(0) #remove와 다르게 꺼낸 것이기 때문에 해당 내용 저장하면 재사용 가능
print(f'nums : {len(nums)}개, {nums}')
print(a)
# print(f'a : {len(a)}개, {a}')

# [7] 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지 카운팅해주는 메서드 => count(데이터)
print(nums.count('A'))
print(nums.count(-3))

# [8] 리스트를 확장시키는 메서드=> extend(여러 개 데이터 저장한 데이터 타입)
nums.extend([11,22,33]) # 원본 문자열이 바뀜
print(f'nums : {len(nums)}개, {nums}')
# a = [1, 2, 3]
# b = [4, 5, 6]
# print( a+b, a, b) #이렇게 만들면 원본 데이터에 변화는 없음

nums.extend([])
print(f'nums : {len(nums)}개, {nums}')

nums.extend("새해 복 많이 받으세요") #공백 포함 모두 들어감, 이건 int
print(f'nums : {len(nums)}개, {nums}') # nums : 16개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요']

nums.extend(["새해 복 많이 받으세요"]) #공백 포함 모두 들어감, 이건 list
print(f'nums : {len(nums)}개, {nums}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']

# nums.extend(2024) #TypeError: 'int' object is not iterable
# print(f'nums : {len(nums)}개, {nums}') #시퀀스 또는 반복가능한 데이터만 가능

# [9] 리스트를 복사해주는 메서드 => 얕은 복사()
nums.append([100,200])
nums2 = nums.copy() #복사본이 나오므로 저장해야 함
print(f'nums : {len(nums)}개, {nums}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']
print(f'nums2 : {len(nums)}개, {nums2}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']


# nums의 -1번 요소의 데이터를 2024로 변경
nums[-2]=2024
print(f'nums : {len(nums)}개, {nums}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']
print(f'nums2 : {len(nums)}개, {nums2}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']
# nums2는 새해 복 많이 받으세요가 덩어리라서 2024로 안 바뀜

# nums의 -1번 요소의 0번 요소를 77로 변경
nums[-1][0]=77
print(f'nums : {len(nums)}개, {nums}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']
print(f'nums2 : {len(nums)}개, {nums2}') # nums : 17개, [True, 11, 22, 33, '새', '해', ' ', '복', ' ', '많', '이', ' ', '받', '으', '세', '요', '새해 복 많이 받으세요']
# nums2도 77로 바뀜 - 리스트에는 해당 리스트의 원소별 주소가 있기 때문에
# 얕은 복사는 해당 리스트의 주소가 있기 때문에 원소만 바꾸는 것이고
# 깊은 복사는 주소를 가진 복사본 리스트가 생겨서 두 개의 리스트에서 각각 운영돼야 함
# python tutor에서 확인해보기-------------------------------------------
# aList = [11, 22, [1, 2]]
# bList = aList.copy()
#
# print(aList, bList, sep='\n')
# print(id(aList), id(bList), sep='\n')
# print(id(aList[-1]), id(bList[-1]), sep='\n')
#
# aList[-1][0]='A'
# print(id(aList), id(bList), sep='\n')
# print(id(aList[-1]), id(bList[-1]), sep='\n')
# -----------------------------------------------------------------