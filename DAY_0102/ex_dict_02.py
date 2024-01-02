# ---------------------------------------------------------------
# 다양한 dict 자료형 => key:value <= 데이터 덩어리
# - key로 데이터를 찾기/읽기/삭제/변경
# - key 중복 X => 마지막 데이터의 key의 값으로 저장
# ---------------------------------------------------------------
# 이름, 점수 저장하기
jumsuDict = {'Hong' : 100, 'Park' : 98, 'Kim' : 88, 'Hong' : 50, 'Hong' : 77}

print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}')

# 이름/번호를 키로 해서 점수를 저장 하기 ---------------------------------
# jumsuDict = {['Hong',1] : 100, ['Park',3] : 98, ['Kim',3] : 88, ['Hong',4] : 50, ['Hong',2] : 77}
# print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}') #TypeError: unhashable type: 'list'
# 리스트는 변경가능하기 때문에 키값이 될 수 없음

jumsuDict = {('Hong',1) : 100, ('Park',3) : 98, ('Kim',3) : 88, ('Hong',4) : 50, ('Hong',2) : 77}
print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}')

print(f"jumsuDict[('Hong', 2)] => {(jumsuDict[('Hong', 2)])}")

print(f"jumsuDict[('Hong', 1)] => {(jumsuDict[('Hong', 1)])}")

# 키의 데이터 타입 동일해야 하나요? 아닙니다.
testDict = { 1 : 'Hong', 2.0 : 'Kim', False : 100, "name" : 'HongGilDong', False : 2024}
print(f'testDict => {len(testDict)}개,{testDict}')

# 빈 딕셔너리 생성
emDict = {}
print(f'emDict => {type(emDict)}, {len(emDict)}개')

# Bool Type 으로 보면
a = []
b = ()
c = {}

print(bool(a), bool(b), bool(c)) # 0이기 때문에 False False False