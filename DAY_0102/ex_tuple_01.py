# ----------------------------------------------------------------
# 튜풀(Tuple) : 읽기 전용의 리스트라고 함
# - 저장 후 수정, 삭제, 추가, 변경 안됨!
# - 용도 : 변경되면 안되는 데이터를 저장
# - 예시 : 성별, 주미번호, 국가코드, 프로그램 상에서 변경되면 안되는 데이터
# - 문법 : (데이터1, 데이터2, ..., 데이터n)
#         데이터1, 데이터2, ..., 데이터n
#         (데이터1,) 또는 데이터1,         반드시 ','가 있어야 함
# ----------------------------------------------------------------
# 다르프로그램은 변수는 계속 데이터 변경, 상수는 변경 안됨
# 그러나 파이썬은 전부 변수이기 때문에, 튜플 만을 변경되는 안되는 Data로 저장하는 타입 제공
# 튜플 데이터 생성----------------------------------------------------
# 성별, 주민번호를 저장하기
# myInfo = ['F', '123456-1234567'] 인 경우 변경가능하기 때문에
myInfo = ('F', '123456-1234567')
print(f'myInfo => {type(myInfo)}, {myInfo}')

# 성별 데이터 읽기
print(f'myInfo => {type(myInfo)}, 성별 : {myInfo[0]}')
print(f'myInfo => {type(myInfo)}, 주민등록번호 : {myInfo[-1]}')

# 성별 데이터 변경 ==> 여자에서 남자로
# 미지원 기능
# myInfo[0] = 'M' #TypeError: 'tuple' object does not support item assignment

# 성별 데이터 삭제 == 미지원
# del myInfo[0] #TypeError: 'tuple' object doesn't support item deletion

# 생일 데이터 추가 == 미지원

# 튜플 ==> 리스트 형변환
myInfo = list(myInfo)
print(f'myInfo => {type(myInfo)}, {myInfo}')

myInfo[0] = 'M'
print(f'myInfo => {type(myInfo)}, {myInfo}')

myInfo[1].replace('2','3',1)
print(f'myInfo => {type(myInfo)}, {myInfo}')


# 리스트 ==> 튜플
myInfo = tuple(myInfo)

# 변수 재선언하는 것도 가능한 듯..수업에선 안함
myInfo = "남자"
print(f'myInfo => {type(myInfo)}, 성별 : {myInfo[0]}')

myInfo = ('M', '123456-1234567')
print(f'myInfo => {type(myInfo)}, 성별 : {myInfo[0]}')


# ----------------------------------------------------------------
# 1개 원소를 가진 튜플 생성
# ----------------------------------------------------------------
myData= '82'   #는 str을 저장
print(f'type(myData): {type(myData)}')
myData2= ('82')   #는 str을 저장 / 그저 가독성 향상용일 뿐
print(f'type(myData): {type(myData2)}')
myData3= '82',  #는 tuple로 저장
print(f'type(myData): {type(myData3)}')
myData4= ('82',)  #는 tuple로 저장
print(f'type(myData): {type(myData4)}')

# ----------------------------------------------------------------
# 리스트 안에 원소/요소 데이터가 몇 개 존재하는 지 카운트를 알려주는 메서드 count(원소데이터)
a = [1, 2, 1, 1, 5, ['A', 'C'], 1, 1, ['A', 'C']]

print(a.count(1))
print(a.count(['A','C']))
print(a.count('A'))
print(a.count(['A']))