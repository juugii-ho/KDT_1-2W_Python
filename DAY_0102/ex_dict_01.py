# ---------------------------------------------------------------
# [질문] 10명 학생에 대한 학점을 젖아 하기
# - 학생의 이름과 학점
# 방법1) 학생 이름 변수 10개 => stdName1 ~ stdName10
#       학점변수 10개      => jumsu1 ~ jumsu10

stdNum01 = 'std01'
stdNum02 = 'std01'
stdNum03 = 'std01'
stdNum04 = 'std01'
stdNum05 = 'std02'
stdjumsu01 = ('90')
stdjumsu01 = ('89')
stdjumsu01 = ('100')
stdjumsu01 = ('76')
stdjumsu01 = ('34')


#한 개의 변수 이름으로 10개의 정보를 관리하고 싶을 때 사용
# 방법2) 학생 이름 변수 10개 => stdNames=[학생 이름1, ...,  학생 이름5]
#       학점변수 10개      => stdJumsus=[점수1, ..., 점수5]
stdNums = ['std01', 'std02', 'std03', 'std04', 'std05']
stdJumsus = [90, 89, 100, 76, 34]

# => 학번03번 학생의 학번과 점수를 출력하세요
idx = stdNums.index('std03')
print(f"{stdNums[idx]}학번 학생의 점수 {stdJumsus[idx]}점")


# 방법3) 학생 이름 변수 10개 => stdNames=[학생 이름1, ...,  학생 이름5]
#       학점변수 10개      => stdJumsus=[점수1, ..., 점수5]
stdNumsJumsu=[['std01',90], ['std02', 89], ['std03', 100], ['std04', 76], ['std05', 34]]
print(stdNumsJumsu)


# ---------------------------------------------------------------
# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# - 형태 => 키 : 데이터    ( 예시 => 주민번호 : 이름, 학번 : 전공 )
# - 조건 => 키가 중복되면 안됨!
# - 문법 => {키1 : 데이터1, 키2: 데이터2, ... 키N : 데이터N} dict
#          [ 데이터1, 데이터2, ..., 데이터n] 리스트
#          ( 데이터1, 데이터2, ..., 데이터n) 튜플
# ---------------------------------------------------------------
stdNumsJumsu = {'std01' : 90, 'std02' : 89, 'std03' : 100, 'std04' : 76, 'std05' : 34}
                        # 0             1             2              3             4
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {type(stdNumsJumsu)}, {stdNumsJumsu}')

# 원소 읽는 방법 => 변수명[Key]
print(f'stdNumsJumsu : {stdNumsJumsu["std03"]}')

# 마지막 원소 지정하는 -1 사용 => -1에 대한 키가 없으면 ERROR.
#print(f'stdNumsJumsu[-1] => {stdNumsJumsu[-1]}') 인덱스 없음. [-1], [0] 등 불가


# ---------------------------------------------------------------
# 원소/요소 추가 방법 => 변수명[새로운 키] = 데이터
# ---------------------------------------------------------------
stdNumsJumsu['std10'] = 99.8
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {type(stdNumsJumsu)}, {stdNumsJumsu}')

# ---------------------------------------------------------------
# 원소/요소 데이터 변경  => 변수명[기존 키] = 새로운 데이터
# ---------------------------------------------------------------
# 학번 10인 학생의 점수 99점으로 변경
stdNumsJumsu['std10'] = 99
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {type(stdNumsJumsu)}, {stdNumsJumsu}')

# ---------------------------------------------------------------
# 원소/요소 데이터 tkrwp  => del 변수명[키] 또는 del(변수명[키])
# ---------------------------------------------------------------
del stdNumsJumsu['std10']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {type(stdNumsJumsu)}, {stdNumsJumsu}')

del (stdNumsJumsu['std02'])
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {type(stdNumsJumsu)}, {stdNumsJumsu}')

# 키는 값을 변경할 수 없기 때문에 튜플만 가능, 리스트 불가, 중복일 경우 뒤의 값만 인식