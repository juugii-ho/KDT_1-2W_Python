# # -----------------------------------------------------------------
# # 다양한 함수의 형태 - 특별한 함수 (2)
# # - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# # - 키와 값의 덩어리 데이터
# # - 형태 : def 함수명(**data):
# # - 이름 : 가변 인자 함수
# # - 매개변수 갯수 : 0개 ~ N개
# # - 호출 : 함수명(키1=값1)
# #         함수명(키1=값1, 키2=값2, 키3=값3) 형태
# #         함수명()
# # -----------------------------------------------------------------
# aDict = {'name':'Hong', 'age':10}
# aDict.update(job = '학생')
# aDict.update(job = '학생', birth='1112', blood='A')
# print(aDict)
# aDict.update(점수1 = 100, 점수2 = 200, 점수3 = 300, 점수4 = 400, 점수5 = 500)
# print(aDict)
#
# def addx(x,y):
#     '''
#     x+y
#     :param x: int
#     :param y: int
#     :return: x + y int
#     '''
#     return x+y
#
# print(addx (1, 2))

# -----------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일, ...
#           가변 + 데이터 정보 함께
#           키워드파라미터 **member
# 반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------------

def joinMember(**member):
    # print(type(member))
    # 멤버 저장소에 멤버 추가하기
    mList.append(member)

    members[f'M{len(members)+1}'] = member

    print(member)
    print(mList)
    pass

#
#
# # -----------------------------------------------------------------
# # 함수 사용 즉 호출
# # -----------------------------------------------------------------
# # 가입된 회원들 저장 변수
members = {}
mList = []
#
print(f'[BF] : {members}')

# # 회원가입 기능 함수 호출
joinMember(name='Hong', age=17, birth='2020')
joinMember(id='Hong84', phone='010', job='actor', blood='B')
joinMember(id='Hon', birth='2012', blood='AB')

print(f'[AF] : {members}')

#
# # m = {'name':'Hong', 'age':17}
# print("key", members.keys())
# print(members.values())
# print(members.items())
#
# joinMember(name='Hong', age=17, birth='2222/22/22')
# print("key", members.keys())
# print(members.values())
# print(members.items())

# -----------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember2
# 매개 변수 : 필수 => id, pw
#           선택 => **option 이름, 전화번호, 이메일, 취미, 주소, 생일, ...
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------------

def joinMember2(id, pw, **option): #**option, id, pw는 앞이 몇개 들어올 지 모르기때문에 가변 인자가 뒤로 와야
    # 멤버 저장소에 멤버 추가하기
    print('ok')

members = {}
mList = []
#
print(f'[BF] : {members}')

# # 회원가입 기능 함수 호출
joinMember2(id='Hong', pw=1234, age=17, birth='2020')
joinMember2(id='Hong84', pw='010', job='actor', blood='B')
# joinMember2(id='Hon', birth='2012', blood='AB')

print(f'[AF] : {members}')
print(f'[AF] : {mList}')



# -----------------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember3
# 매개 변수 : 필수 => id, pw
#           선택 => **option 이름, 전화번호, 이메일, 취미, 주소, 생일, ...
#           가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.' str
# -----------------------------------------------------------------

def joinMember3(id, pw, loc='내국인', gender='남자', **option): #**option, id, pw는 앞이 몇개 들어올 지 모르기때문에 가변 인자가 뒤로 와야
    # 멤버 저장소에 멤버 추가하기
    print(id, pw, loc, gender, option)
    # 키 => id
    # 값 => pw, loc='내국인', gender='남자', **option
    #       { 'pw' : '1234', 'loc' : '내국인', 'gender' : '남자', **option 반복문해서 풀든가, 'etc': option 하든지}
    valueDict = {}
    valueDict['pw'] = pw
    valueDict['loc'] = loc
    valueDict['gender'] =gender
    valueDict['etc'] = option
    members[id] = valueDict



members = {}
mList = []
#
print(f'[BF] : {members}')

# # 회원가입 기능 함수 호출
joinMember3(id='Hong', pw='1234', age=17, birth='2020')
joinMember3(id='Hong84', pw='10', gender='여자', job='actor', blood='B')
joinMember3('Hon', '2012', '내국인')

print(f'[AF] ---------')
for m in members.items():
    print(m)

def test2(gojung, *a, **kw):
    print(gojung, a, kw)



test2(10, 20, 30, name=('Hong','lee', 'kim'))

print(test2)