# -----------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수 정해 지지 않은 경우
# -----------------------------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 입력 받은 데이터 저장해 주세요.
#
# saves = ""
# while not saves in ("x", "X") :
#     saves = input("저장하고 싶은 내용을 작성해주세요(종료버튼은 x입니다): ")
# print("프로그램을 종료합니다.")
#
# while True:
#     data=input("저장하고 싶은 데이터 입력(종료 x): ")
#     # 종료 검사
#     if data in ('x', 'X'): break
#     print("OK")
# print("프로그램 종료")
#
#
#
# print('box' in "boxyze")        # box가 있어서 가능
# print('bo' in ('boA', 'boC'))   # ('boA', 'boC')가 1개의 원소라 안 됨
#
#

# -----------------------------------------------------------------
# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#       입력 받은 정수만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 5
#       abcde
#       출력 원하는 알파벳 수 입력 : 1
#       a
#       출력 원하는 알파벳 수 입력 : 10
#       abcdefghij
#       출력 원하는 알파벳 수 입력 : 27
#       abcdefghijklmnopqrstuvwxyz 종료
#       출력 원하는 알파벳 수 입력 : 1
#       a
#       출력 원하는 알파벳 수 입력 : x
#       종료
# -----------------------------------------------------------------

# num = int(input("출력을 원하는 알파벳 수를 입력해주세요: "))
# alp = "a", "b", "c", "d"
# while num>0:


#
# while True:
#     num = input("출력 원하는 알파벳 수 입력: ")
#     # 무한 입력 반복 종료 조건
#     if num in ('x', 'X'):
#         print("종료입니다.")
#         break
#     num = int(num)
#     aCode = ord('a')
#     while aCode+num =
Test = False

if Test:
    while True:
        count = input("출력 원하는 알파벳 수 : ")
        if count in ('x', 'X'):
            print("프로그램 종료됩니다.")
            break
        if count.isdecimal():
            count=int(count)

            aCode = ord('A')
            for value in range(count):
                value += aCode
                print(f'value => {value}, {chr(value)}')
                # print(f'{chr(value)}', end='\n완료\n"' if value == ord('Z') else '')
                if value == ord('Z'): break
        else:
            print("유효한 데이터가 아닙니다.")

    print("----코드 끝 부분----")
# 코드값 0은 48, A는 65, a는 97 정도는 기억하자

# isEnd = False       # flag 함수
# for n in range(100):
#     if isEnd:
#         print("프로그램 종료합니다.")
#         break
#     print(f"out -> {n}")
#
#     for n2 in range(100):
#         if n2>10:
#             isEnd = True
#             break
#         print(f"in -> {n2} ===> {n}번째")
#
isEnd = False
outCnt = 0
while outCnt < 100 :
    if isEnd :
        print('프로그램 종료')
        break
    print(f'out -> {outCnt+1}')
    outCnt += 1
    inCnt = 1
    while inCnt < 100:
        if inCnt >10:
            isEnd = True
            break
        print(f'in -> {inCnt} ===> {outCnt}번째')
        inCnt += 1
print("ㄴ내가 만든것 \n")

# 내가 만든 것

# -----------------------------------------------------------------

# 선생님이 만든 것

# [요청] 내부에 반복문에서 데이터가 10초과되면 프로그램을 종료 ------------
isEnd = False
outNum= 1
while outNum<=100:
    if isEnd :
        print("외부 요청으로 프로그램을 종료합니다.")
        break
    print(f'outNum => {outNum}')

    # 내부 while
    inNum = 1
    while inNum<=100:
        if inNum > 10 :
            print("내부 요청으로 프로그램을 종료합니다.")
            isEnd = True
            break
        print(f'inNum => {inNum} ====> {outNum}번째')
        inNum += 1

        outNum += 1

# -----------------------------------------------------------------
