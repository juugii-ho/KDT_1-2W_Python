# [문제] --------------------------------------------------
# 문자열 여러 개와 실수 숫자 여러 개를 두 줄로 입력 받기
# - 첫 번째 입력 받은 값은 Key
# - 두 번째 입력 받은 값은 Value
# - 딕셔너리로 저장해 주세요.
# --------------------------------------------------------

# 12.5 기존에 내가 풀었던 방식
# 입력 값이 4개일 때랑 5개일 때 구분을 못하는 게 문제. 5개일 때만 실행가능

# keys = input().split(' ')
# values = input().split(' ')
# if bool(keys[4]) == True:
#     print(f''' {(keys[0])} :{values[0]}, {keys[1]}:{values[1]}, {keys[2]}:{values[2]}, {keys[3]}:{values[3]}, {keys[4]}:{values[4]}''')
# else:
#     print(f''' {keys[0]} :{values[0]}, {keys[1]}:{values[1]}, {keys[2]}:{values[2]}, {keys[3]}:{values[3]}''')
#
# print(bool(keys[4]))


# 선생님 방법 -------------------------------------------------
twoData = input("문자열 4~5개, 실수 숫자 4~5개를 두 줄로 입력\n단, 문자열과 실수 갯수는 동일 \n(예: aa bb cc dd, 3.1 5.2 6.5 8.1) :")
# 두 줄로 입력을 받는 다른 방법이 아닌 ','나 '\'로 구분할 수 있게끔 예시를 주는 식으로 제공
# 받은 입력을 내가 ','나 '\' 기준으로 다시 줄바꿈 하는 것

# key와 value로 데이터 분리
datas = twoData.split(',')
keys = datas[0].split()
values = datas[1].split()


# 입력 데이터 존재 여부 체크
if (len(keys)==4 and len(values)==4) or (len(keys)==5 and len(values)==5):
    print("입력이 완료되었습니다.")
    dataDict = {}
    if len(keys) ==4:
        dataDict[keys[0]] = float(values[0])
        dataDict[keys[1]] = float(values[1])
        dataDict[keys[2]] = float(values[2])
        dataDict[keys[3]] = float(values[3])
        print(dataDict)
    else:
        dataDict[keys[0]] = float(values[0])
        dataDict[keys[1]] = float(values[1])
        dataDict[keys[2]] = float(values[2])
        dataDict[keys[3]] = float(values[3])
        dataDict[keys[4]] = float(values[4])
        print(dataDict)

else:
    print("입력된 데이터가 정확하지 않습니다.")


# 양식에 맞게끔 입력하는 지 확인하는 과정 필수...귀찮더라도 해야