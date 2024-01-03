# --------------------------------------------------------
# 컴프리헨션 (comprehension)
# - List Comprehension, Dict Domprehension, Set Comprehension
# - 튜플은 변경이 안 돼서 없음
# --------------------------------------------------------
# [실습1] aList의 원소 값을 제곱한 값을 원소로 가지는 bList를 생성하세요.

# 일반적 for 방식
aList = [1, 2, 3, 4]

bList = []

for a in aList:
    bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컴프리헨션 - list와 for문 합치기
cList = [ a**2 for a in aList ] # 대량 작업 시 메모리 처리, 속도 더 좋음
print(f'cList => {cList}')



# [실습2] aList의 원소 값 중에서 짝수인 데이터만 제곱한 값을 원소로 가지는 bList를 생성하세요.
aList = [1, 2, 3, 4]
bList = []
for a in aList:
    if not a%2:             # not False => True
        bList.append(a**2)

cList =[]
for a in aList:
    if a%2==0:              # 두 식 다 할 줄 알아야 함
        cList.append(a**2)

print(aList)
print(bList)
print(cList)

# 컴프리헨션 방식

cList2 = [ a**2 for a in aList if not a%2 ]
#          ---- -------------- -----------
#          (3)       (1)           (2)
# (2) 에서 True인 경우만 (3) 실행
# 연산자 우선순위는 아니고 이 순서가 문법임. 하나 외워두는 게 나을 듯..?
print(f'cList2 => {cList2}')


# --------------------------------------------------------
# 컴프리헨션 (comprehension)
# - List Comprehension, Dict Domprehension, Set Comprehension
# --------------------------------------------------------
# [실습1] aList의 원소 값을 제곱한 값을 원소로 가지는 bList를 생성하세요.

# 일반적 for 방식
aList = [1, 2, 3, 4]

bList2 = []

for a in aList:
    bList2.append(a**2)

print(f'aList => {aList}')
print(f'bList2 => {bList2}')

# 컴프리헨션 - list와 for문 합치기
cList = [ a**2 for a in aList ] # 대량 작업 시 메모리 처리, 속도 더 좋음
print(f'cList => {cList}')



# [실습3] aList의 원소 값 중에서 짝수인 데이터만 제곱, 홀수인 데이터는 그대로 저장한 bList를 생성하세요.
aList = [1, 2, 3, 4]
bList3 = []

for a in aList:
    if not a%2:
        bList3.append(a**2)
    else:
        bList3.append(a)
print(f'aList => {aList}\nbList3 => {bList3}')

# 컴프리헨션
cList3 = [ a**2 if not a%2 else a for a in aList ] # 이걸 외우자 ㅋㅋ
#          ---- ---------- ------ --------------
#          (3-T)     (2)    (3-F)      (1)
print(f'cList3 => {cList3}')

# 딕셔너리 컴프리헨션 (키값만 잘 잡아주고, {}로만 바꿔주면 됨)
cList3 = { a :a**2 if not a%2 else a for a in aList }
#          ---- ---------- ------ --------------
#          (3-T)     (2)    (3-F)      (1)
print(f'cList3 => {cList3}')