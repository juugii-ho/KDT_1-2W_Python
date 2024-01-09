# ----------------------------------------------------------
# 전역 변수(Global Variable)와 지역 변수(Local Variable)
# - 함수 내에서 전역 변수 값 변경하고자 하는 경우는 추가 코드 필요
# - 추가 코드 : global 전역 변수명
# -> 주의 : 전역 변수 값이 언제 든지 함수로 변경이 될 수 있는 상황
#          사용 시에 주의 필요함
# ----------------------------------------------------------
# 사용자 정의 함수 -------------------------------------------
def currentDate(todays, week):
    # todays => 년, 월, 일을 원소로 담고 있는 데이터 타입, 리스트
    todays[0] = todays[0]+100
    print(f'Today : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}')

# 전역 변수 ---------------------------------------------------
year, month, day, week = 2024, 1, 8, 'Mon'
todayList = [year, month, day]

# 함수 사용 즉 함수 호출 -----------------------------------------
print(f'year : {year}, month : {month}, day : {day}, week : {week}')
print(todayList)
currentDate(todayList, week)

# 변수값 확인 출력
print(f'year : {year}, month : {month}, day : {day}, week : {week}')
print(todayList)