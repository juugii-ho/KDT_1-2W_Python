fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)  # 세트는 순서 정해져있지 않음

fruits = {'orange', 'orange', 'cherry'}
print(fruits)

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}

# print(fruits[0])    #TypeError: 'set' object is not subscriptable
# print(fruits['strawberry']) # TypeError: 'set' object is not subscriptable
# 세트는 []대괄호로 특정 요소만 출력할 수 없음

print('orange' in fruits)       # True
print('peach' in fruits)        # False

print('peach' not in fruits)        # True
print('orange' not in fruits)       # Fals

a = set('apple')
print(a)            # {'p', 'a', 'l', 'e'} 순서 상관 없이 출력
b = set(range(5))
print(b)            # {0, 1, 2, 3, 4} 는 순서 안 바뀌고 출력

c = set()
print(c)            # set()

c = {}
print(type(c))      # <class 'dict'>
c = set()
print(type(c))      # <class 'set'>
print(set('안녕하세요'))     # {'하', '요', '녕', '안', '세'}

# print(a = {{1,2}, {3,4}})   # set 안에 set 못 넣음

a = frozenset(range(10))
print(a)            # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# print(a |= 10)         # | 등의 연산 불가
# print(a.update({10})     # 추가 불가


a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)                  # {1, 2, 3, 4, 5, 6}
print(set.union(a,b))    # {1, 2, 3, 4, 5, 6}

print(a&b)                             # {3, 4}
print(set.intersection(a,b))        # {3, 4}

print(a - b)                           # {1, 2}
print(set.difference(a,b))          # {1, 2}

print(a ^ b)           # 대칭차집합        # {1, 2, 5, 6}
print(set.symmetric_difference(a, b))   # {1, 2, 5, 6}

a = {1, 2, 3, 4}
a |= {5}
print(a)                    # {1, 2, 3, 4, 5}

a = {1, 2, 3, 4}
a.update({5})
print(a)                    # {1, 2, 3, 4, 5}

a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}        # &는 교집합 요소만 저장
print(a)                    # {1, 2, 3, 4}
a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
print(a)

a = {1, 2, 3, 4}
a -= {3}
print(a)                    # {1, 2, 4}
a = {1, 2, 3, 4}
a.difference_update({3})
print(a)

a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)                    # {1, 2, 5, 6}
a = {1, 2, 3, 4}
a.symmetric_difference_update({3,4,5,6})
print(a)                    # {1, 2, 5, 6}

a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})        # True
print(a.issubset({1,2,3,4,5}))  # True issubset = '같거나 작다'

a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5})      # True

a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})        # True
print(a.issuperset({1,2,3,4}))  # True issuperset = '같거나 크다'

a = {1, 2, 3, 4}
print(a > {1, 2, 3})            # True

a = {1, 2, 3, 4}
print( a == {1, 2, 3, 4})       # True
# print( a is {1,2,3,4})         # False
print( a == {4, 2, 1, 3})       # True

a = {1, 2, 3, 4}
print(a != {1, 2, 3})

a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))   # True  세트끼리 겹치는지 확인
print(a.isdisjoint({3, 4, 5, 6}))   # False

a = {1, 2, 3, 4}
a.add(5)
print(a)

a.remove(3)         # 삭제, 없으면 에러
print(a)

a.discard(2)        # 삭제, 없으면 넘어감
print(a)

a.discard(3)
print(a)

a.clear()
print(a)

a = {1,2,3,4}
print(len(a))

a = {1,2,3,4}
b = a
print(a is b)       # True
b.add(5)
print(a)            # {1, 2, 3, 4, 5}
print(b)            # {1, 2, 3, 4, 5}

a = {1,2,3,4}
b = a.copy()
print(a is b)       # False
print(a == b)       # True

a = {1,2,3,4}
b = a.copy()
b.add(5)
print(a)            # {1, 2, 3, 4}
print(b)            # {1, 2, 3, 4, 5}


a = {1, 2, 3, 4}
for i in a:
    print(i)
for i in {1, 2, 3, 4}:
    print(i)


a = {i for i in 'apple'}
print(a)            # {'e', 'l', 'a', 'p'} 세트라서 순서바뀜

a = {i for i in 'pineapple' if i not in 'apl'}
print(a)            # {'e', 'i', 'n'} 세트라서 순서바뀜

a = 10
b = 20

aList = []
bList = []
for aL in range (1, a+1):
    if a % aL == 0:
        aList.append(aL)
for bL in range (1, b+1):
    if b % bL ==0:
        bList.append(bL)
cList = set(aList)&set(bList)
        # cList.pop(0)
print(cList)
# print(max(cList))
print(aList)
print(bList)
# # for aL in aList:
# #     cList.append(aL & bL)
# print(cList)

c = {1, 2, 3, 4}

print(c)