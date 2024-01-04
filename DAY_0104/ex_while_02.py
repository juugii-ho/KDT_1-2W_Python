# -----------------------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수가 정해진 경우 사용 가능함
# -----------------------------------------------------------------
# [요청] 사용자가 알고 싶어하는 단을 입력 받아서 해당 단의 구구단을 입력
#       단, while 반복문 사용하기
# [예시] 알고 싶은 단 입력 : 3
#       --3단--
#       3 * 1 = 3
#       3 * 2 = 6
#       3 * 3 = 9
#       3 * 4 = 12
#       3 * 5 = 15
#       3 * 6 = 18
#       3 * 7 = 21
#       3 * 8 = 24
#       3 * 9 = 27
# -----------------------------------------------------------------
TEST = False

if TEST:
    Cnt = 1
    dan = int(input("원하는 구구단 단 수를 입력해주세요: "))
    print(f'{dan:-^11}')
    while Cnt<=9 :
        print(f' {dan} * {Cnt} = {dan*Cnt:>2}')
        Cnt += 1


cnt = 1
dan = 2
while dan <=9:
    print(f"{dan:-^11}", end='\t' if dan != 9 else '\n')
    dan += 1

dan = 2
while not  dan==9:
    cnt = 1
    print(f"{dan} * {cnt} = {dan*cnt:>2}",  end='\t' if dan != 9 else '\n')
    cnt += 1
    dan += 1
cnt = 1

dan, unit =2, '단'
num = 1
while dan < 10:
    print(f'{dan:->5}{unit:-<5}')
    num = 1
    while num<10:
        print(f'{dan}*{num}={dan*num:2}')
        num += 1
    dan += 1