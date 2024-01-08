
'''
1. 문자열 리스트를 입력 받아서 내림차순 결과 가장 낮은 문자열과 가장 높은 문자열을
출력하는 함수를 구현하세요.
[입 력] msg=[‘Good’, ‘child’, ‘Zoo’, ‘apple’, ‘Flower’, ‘ zero’]
[함수호출]
[출 력] 정렬 결과 : ['zero', 'child', 'apple', 'Zoo', 'Good', 'Flower']
가장 높은 문자열 : zero, 가장 낮은 문자열 : Flower
'''

def sortFunc(*data):
    msg = input().split(', ')
    msg = sorted(msg)[::-1]
    print(f'''정렬 결과 : {msg}
    가장 높은 문자열 : {msg[0]}, 가장 낮은 문자열 : {msg[-1]}
    ''')

# sortFunc()

'''
2. 키보드로 입력 받은 데이터 중에서 숫자만 모두 저장하여 합계, 최대값, 최소값을
출력하는 함수를 구현하세요.
[입 력] 데이터 입력 : 하늘 Apple 2021 –9 False 23 7 None 끝
[출 력] 합계 : 2042 최댓값 : 2021 최솟값 : -9
----------------------------------------------------------------------------------------------
[입 력] 데이터 입력 : A 홍길동 False True True None Good Luck 가나다라
[출 력] 합계 : 0 최댓값 : 0 최솟값 : 0
'''

# def func01(*data):
#     data = input().split(' ')
#     intData = []
#     for d in data:
#         if d.isnumeric():
#             d = int(d)
#             intData.append(d)
#     id1 = sum(intData)
#     id2 = max(intData)
#     id3 = min(intData)
#
#     print(f'합계 : {id1}, 최댓값 : {id2}, 최솟값 : {id3}')
#
# func01()

# 왜 isdecimal, isnumeric이 안되는가?
'''
3. 아래 조건을 만족하는 코드를 작성하세요.
- ‘q’, ‘Q’ 입력 전까지 동작
- 대문자 Q 제외한 나머지 알파벳 입력 시 ♠ 출력
- 소문자 q 제외한 나머지 알파벳 입력 시 ♤ 출력
- 0 ~ 9 숫자 입력 시 숫자만큼의 ◎ 출력
'''

# def qQ():
#     data = input()
#     if data.isupper():
#         print("♠")
#     elif data.islower():
#         print("♤")
#     elif data.isnumeric():
#         for d in data:
#             print("◎", end='')
#     else:
#         print("잘못된 입력입니다.")
#
# qQ()

'''
4. 아래 조건을 만족하는 코드를 작성하세요.
- 수의 범위 : 1 ~ 100
- 3의 배수 숫자
- 7의 배수 숫자
- 8의 배수 숫자
- 3, 7, 8의 배수 숫자로 구성된 숫자만 출력
- 단!! 중복된 숫자는 제거 하세요.
'''

# def print378():
#     for data in range(1,101):
#         if data%21==0 or data%24==0 or data%56==0:
#             pass
#         elif data%3 ==0 or data%7==0 or data%8==0:
#             print(data, end=' ')
#
# print378()

'''
5. 문자열을 입력하면 코드값을 아래와 같이 출력해주는 함수를 구현해 주세요.
[입 력] data=“가나다”
[함수호출]
[출 력]"가나다"의 인코딩 : 0xac000xb0980xb2e4
"가나다" 인코딩 : 0b10101100000000000b10110000100110000b1011001011100100
'''

# def hexData():
#     data = input()
#     data2 = ''
#     data3 = ''
#     for d in data:
#         data2 += (hex(ord(d)))
#         data3 += (bin(ord(d)))
#     print(f'''"{data}"의 인코딩 : {data2}
# "{data}"의 인코딩 : {data3}''')
#
# hexData()

'''
6. 문자열 리스트와 정수 1개를 입력하면 아래와 같이 출력하는 함수를 구현해 주세요.
[입 력]
- 1개 이상의 소문자 알파벳 문자열로 이루어진 리스트 datas
- 정수 n
[기 능]
- 리스트의 문자열 요소의 n번째 인덱스부터 오름차순 정렬하기
- 정렬 후 그 결과 반환
- 단! 모든 문자열은 길이가 n보다 큼
- 단! 인덱스 1의 문자가 같은 문자열이 여럿 있을 경우, 사전순 앞선 문자열이 앞쬭에 위치
[ 조건 ]
[입 력] datas : ['askde', 'beach', 'surf'] n=2
[출 력] ['beach', 'askde', 'surf']
[입 력] datas : ['home','pitch','python'] n=1
[출 력] ['pitch', 'home', 'python']
'''

# def nIndex():
#     pass
# datas1 = "datas : ['askde', 'beach', 'surf']"
# datas2 = "n=2"
#
# num=''
# for d2 in datas2:
#     if d2.isdecimal():
#         num += d2
# print(num)
#
# data1_1 = datas1.split('[')
# # data1_2 = {data1_1[0]:data1_1[1]}
# data1_2 = data1_1[1].replace("]",'')
# data1_3 = data1_2.replace("'",'')
# print(data1_3)
# data1_4 = data1_3.split(', ')
# print(data1_4)
# data1_5 = []
# for d in data1_4:
#     data1_5 += d[int(num)]
# print(data1_5)
#
# def func01(data, n):
#     return data[n], data

# 두번째 문자열 비교하는 것 까지 만듦.. 이후는 ...



'''
7. 아래와 같이 출력되는 함수를 구현해 주세요.
[입 력]
- 정수 리스트 nums
[기 능]
- 정수 리스트 안에 2가 포함된 연속된 부분 리스트를 찾아서 반환
- 정수 리스트 안에 2가 1개 포함 된 경우 [2] 반환
- 정수 리스트에 2가 없는 경우 [-1] 반환

[입 력] nums : [ 0, 1, 2, 4, 5, 2, 9 ]
[출 력] [2, 4, 5, 2]
[입 력] nums : [ 0, 1, 2, 4, 5, 2, 9, 3, 2, 8, 1 ]
[출 력] [2, 4, 5, 2, 9, 3, 2]
[입 력] nums : [ 0, 1, 2, 4, 5, 3, 1, 7 ]
[출 력] [2]
[입 력] nums : [ 0, 0, 0 ]
[출 력] [-1]

'''
#
# def count(*nums):
#     inp = input()
#     # print(type(inp))
#     nums = inp.split(": ")[1]
#     print(nums, type(nums))
#     n2 = []
#     for n in nums:
#         if n.isdecimal():
#             # n0 n
#             n2.append(int(n))
#     print(n2)
#     print(type(n2))
#     a = n2.index(2)
#     b = n2.index(2, a + 1)
#     c = n2.index(2, b + 1)
#     nums2 = []
#     print(a,b,c, type(a),type(b),type(c))
#     if c !=0:
#         nums2 = n2[a:c+1]
#     elif b !=0:
#         nums2 = n2[a:b+1]
#     else:
#         nums2 = [2]
#     print(nums2)
#
#
# count()

# nums : [ 0, 1, 2, 4, 5, 2, 9, 3, 2, 8, 1 ]일 때는 구현했는데 나머지 경우는 모르겠음..

'''
8. 아래와 같이 출력된 함수를 구현해 주세요.
[ 조건 ]
[입 력]
- 정수 리스트 nums
[기 능]
- 정수로 이루어진 리스트에서 중복되지 않는 원소 뽑아 그 합이 0이 되는 조합의 수
- 단! 리스트 길이는 3보다 큼

[ 예시 ]
[입 력] nums : [ -2, 3, 0, 2, -5 ]
[출 력] 2
[입 력] nums : [-3, -2, -1, 0, 1, 2, 3 ]
[출 력] 5
'''
#
# def sumZero():
#     pass
#
# nums = "nums : [ -2, 3, 0, 2, -5 ]"
# nums = nums.split(": ")[1]
# print(nums, type(nums))
# waitList = []
# for n in nums:
#     if n.isdecimal():
#         waitList.append(int(n))
# waitTuple = tuple(waitList)
# print(waitTuple, type(waitTuple),sum(waitTuple))
# # for sumN in waitTuple:
# #     T2 = sum(waitTuple)
# # (2, 3, 0, 2, 5) <class 'tuple'> 12 까지 출력하고 끝

'''
9. 아래와 같이 출력된 함수를 구현해 주세요.
[입 력]
- 출력 원하는 단
[기 능]
- 리스트 컨프리헨션(List Conprehension)으로 구현
[입 력] 단 : 3
[출 력]
------------------------- 3단 ---------------------
3 * 1 = 3 3 * 2 = 6 3 * 3 = 9
3 * 4 = 12 3 * 5 = 15 3 * 6 = 18
3 * 7 = 21 3 * 8 = 24 3 * 9 = 27
'''

# def gugudan(gu):
#     gui = []
#     for i in range(1,10):
#         gui.append(f'{gu} * {i} = {gu*i:>2}')
#     # if i in range(1,10)%3==0:
#     #     print(gui)
#     print(f'-'*20+f' {gu}단 '+'-'*20)
#     # print(gui)
#     for i in range(1,len(gui)+1):
#         print(gui[i-1], end="\t\t" if i%3!=0 else "\n")
# gugudan(1)

# ['3 * 1 =  3', '3 * 2 =  6', '3 * 3 =  9', '3 * 4 = 12', '3 * 5 = 15', '3 * 6 = 18', '3 * 7 = 21', '3 * 8 = 24', '3 * 9 = 27']
# 까지 했는데 이거 어떻게 나눌지 모르겠음..
# end if end 꼴로 자꾸 하니까 망한 것


'''
10. 숫자와 콤마로만 이루어진 문자열 data가 주어지면 이때, data에 포함되어있는 자연
수의 합과 가장 작은 수, 가장 큰 수를 출력하는 함수를 구현하세요.
[입 력] data=‘123,42,98,18’
[함수호출]
[출 력] "123,42,98,18"의 합 : 38, 가장 큰 수 : 9, 가장 작은 수 : 1
--------------------------------------------------------------------------------------------------------
[입 력] data=‘1,234’
[함수호출]
[출 력] "1,234"의 합 : 10, 가장 큰 수 : 1, 가장 작은 수 : 4
'''
# def sumMaxMin(*data):
#     # data = "data=‘123,42,98,18’"
#     data = input()
#     data1 = data.split("=")[1]
#     # data2 = data1.replace("‘" or "’" or "'" or ",",'')
#     data2 = []
#     for d2 in data1:
#         if d2.isdecimal():
#             data2.append(int(d2))
#     for d3 in data2:
#         data3 = sum(data2)
#         data4 = max(data2)
#         data5 = min(data2)
#     print(f'{data1}의 합 : {data3}, 가장 큰 수 : {data4}, 가장 작은 수 : {data5}')
#
# sumMaxMin()

'''
11. 업-다운 빙고 게임 기능의 함수를 구현하세요.
- 컴퓨터에서 1 ~ 100 범위에서 임의의 수 하나 선정
- 사용자 입력 숫자와 선정된 수가 동일하면 입력 받기 중단
- 사용자 입력 숫자가 선정 수보다 큰 수인지 작은 수인지 힌트 출력
[ 조건 ]
[ 입력 ] 빙고 넘버 : 3
[ 출력 ] 힌트 - 3보다 큰 수
[ 예시 ]
[ 입력 ] 빙고 넘버 : 5
[ 출력 ] 힌트 - 5보다 작은 수
[ 입력 ] 빙고 넘버 : 4
[ 출력 ] 정답 - *~ 빙고 ~*
'''
import random

# def bingo():
#     ranNum = random.randint(1,100)
#     while True:
#         userNum = int(input("빙고 넘버 : "))
#         if ranNum > userNum:
#             print(f"힌트 - {userNum}보다 큰 수")
#             # continue
#         elif ranNum < userNum:
#             print(f"힌트 - {userNum}보다 작은 수")
#             # continue
#         else:
#             print(f"정답 - *~ 빙고 ~*")
#             break
# bingo()


'''
12. 2, 4, 8 게임은 숫자의 끝 자리가 2, 4, 8로 끝나는 숫자의 경우 다른 문자로 출력하는
게임으로 아래 조건을 만족하도록 구현하자.
- 숫자를 int형 타입으로 input함수를 이용하여 입력받는다.
- 2, 4, 8 숫자가 있을 경우 #을 나타나게 한다.
- 입력받은 숫자가 1000일 경우 1부터 1000 까지에 해당하는 2, 4, 8을
#으로 출력한다.
- 한 줄에 20개씩 출력한다.
[ 조건 ]
[입 력] 게임 정수 입력 : 100
[함수호출]
[출 력] 1#3#567#91011#13#151617#1920
21#23#252627#293031#33#353637#3940
41#43#454647#495051#53#555657#5960
61#63#656667#697071#73#757677#7980
81#83#858687#899091#93#959697#99100
'''
# def game_248():
#     inpNum = int(input("게임 정수 입력 : "))
#     for i in range(1,inpNum+1):
#
#         if i%10==2 or i%10==4 or i%10==8:
#             print("#", end="")
#         else:
#             print(i, end="" if i%20!=0 else "\n")
#
# game_248()

'''
13. 월(Month)을 입력 받아 해당 월(Month)의 영어와 계절을 출력하는 코드를 작성하세요.
- 월(Month)에 해당하지 않는 숫자 입력 시 “잘못된 데이터입니다” 출력
[ 조건 ]
[입 력] 좋아하는 월 입력 : 3
[출 력] March Spring
-------------------------------------------------------------------------------------------------------
[입 력] 좋아하는 월 입력 : 15
[출 력] 존재하지 않는 월입니다.
# '''
# def monthSeason():
#     num = int(input("좋아하는 월 입력 : "))
#     month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     season = ["Spring", "Summer", "Fall", "Winter"]
#     moResult = ""
#     seResult = ""
#     if 3<=num<=5:
#         seResult = season[0]
#     elif 6<=num<=8:
#         seResult = season[1]
#     elif 9<=num<=11:
#         seResult = season[2]
#     elif num == 12 or 1<=num<=2:
#         seResult = season[3]
#     else:
#         return print("존재하지 않는 월입니다.")
#     return print(f'{seResult} {month[num-1]}')
#
# monthSeason()

'''
14. 숫자와 화폐단위 입력 받아 세자리 마다 쉼표(,) 찍어서 출력하는 기능을 구현하세요.
- 입력은 함수에 넣지 않습니다.
- 세자리 마다 쉼표(,)와 화폐 단위를 구성해서 출력하는 사용자 정의 함수 생성
[ 조건 ]
[입 력] 숫자 입력 : 1234567, $
[출 력] 1,234,567$
-------------------------------------------------------------------------------------------------------
[입 력] 숫자 입력 : 907, \
[출 력] 907\
'''
# def won3():
#
#     data = input("숫자 입력 : ").split(', ')
#     data1 =int(data[0])
#     print(f"{'{0:,}'.format(data1)}{data[1]}")
#
# won3()


'''
15. 입력받은 숫자 월(Month)에 대한 영어와 한국어 표기를 출력하는 함수를 구현하세요.
[입 력] 좋아하는 월 : 3
[함수호출]
[출 력] March 삼월
'''
#
# num = int(input("좋아하는 월 : "))
#
# def monKorEng(num):
#     if 1<=num<=12:
#         monKor = ["일월", "이월", "삼월", "사월", "오월", "유월", "칠월", "팔월", "구월", "시월", "십일월", "십이월"]
#         monEng = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#         print(monEng[num-1], monKor[num-1])
#     else:
#         return print("잘못된 입력입니다.")
#
# monKorEng(num)

'''
16. 입력받은 정수 2개에 대한 공약수를 모두 출력하는 함수를 만들어 주세요.
-약수란?
특정한 수를 다른 수로 나누었을 때, 그 나머지가 0이되는 수
-공약수란?
두 수가 공통으로 갖고 있는 약수
[ 조건 ]
[입 력] 약수 구하고 싶은 수 : 10 20
[함수호출]
[출 력] 8의 약수 : 1, 2, 5, 10
'''

def gongY():
    gongA = []
    gongB = []
    num1, num2 = map(int, input("약수 구하고 싶은 수 : ").split(" "))

    if num1 >= num2:
        for n in range(1,num2+1):
            if num1%n==0:
                gongA.append(n)
        print(f"{max(gongA)}의 약수 : {gongA}")
    else:
        for m in range(1,num1+1):
            if num2%m==0:
                gongB.append(m)
        print(f"{max(gongB)}의 약수 : {gongB}")

gongY()