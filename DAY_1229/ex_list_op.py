# ------------------------------------------------------------
# List 자료형의 연산 살펴보기
# - 산술연산
# - 비교연산
# - 멤버연산자
# ------------------------------------------------------------
#
# 1~50 범위의 2의 배수로 구성된 리스트 생성

twoNums = list(range(2,51,2))
print(twoNums)

# 산술연산 => 덧셈(+), 곱셈(*)-------------------------------------
datas = twoNums + ["A", "B"] #뒤에 추가됨, List끼리만 가능
print(datas)

# list + str => list + list(str)
# datas = (twoNums + "ABC") #List끼리만 가능
datas = (twoNums + list("ABC")) # 마지막에 A, B, C로 추가됨
print(list("ABC"))
print(datas)

# list + str => str(list) + str
print(str(twoNums) + "ABC") #[~]ABC 가 됨
aa=str(twoNums)
print(aa[0]) # [ 나옴

# list * int => int만큼 원소를 반복해서 하나의 List로 만듦
print(twoNums * 3)


# list + int => list + list(int)
# datas = (twoNums + 11) #List끼리만 가능
# datas = (twoNums + list(11)) #List끼리만 가능
# print(list(11))
# print(datas)


# 멤버 연산 => in / not in ----------------------------------------
#         => 결과 : True / False
print(datas)
print("C" in datas)
print(2 in datas)