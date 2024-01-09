# ----------------------------------------------------------
# 주의! 꼭 전역변수가 아니어도 list, tuple, set, dict의 경우
# 함수의 매개변수로 전달 후 원소값 변경 시 모두 적용이 됨!
# ==> 해결 => 깊은 복사 deepcopy로 복사본 전달 필요!
# ----------------------------------------------------------

def one(number):
    # number : 지역변수
    print(number)

def datas(nums, value):
    # nums : 리스트
    # value : 정수
    nums[-1] = 1004
    print(nums, value, sep=" - ")

# 전역 변수 선언 ----------------------------------------------
value = 'Good'
dataList = [11, 22, 33]
num = 7

# 함수 호출 # def foo():
#     x = 10      # foo의 지역 변수
#     print(x)    # foo의 지역 변수 출력
#
# foo()
# print(x)        # 에러. foo의 지역 변수는 출력할 수 없음
print(f' 전역변수 값 => value : {value}, dataList : {dataList}, num : {num}')
# 전역변수 값 = > value: Good, dataList: [11, 22, 33], num: 7

one(num)                    # num에는 객체 7의 주소
datas(dataList, value)      # dataList에는 dataList 리스트의 주소

print(f' 전역변수 값 => value : {value}, dataList : {dataList}, num : {num}')
# 전역변수 값 = > value: Good, dataList: [11, 22, 1004], num: 7
# dataList 리스트의 주소값만 가져온 것이기 때문에 리스트 내부 원소의 값이 바뀐 것이 반영됨

# 교재 33장(p.419)
# 변수의 사용범위(scope)