# # --------------------------------------------------------
# # [실습1] 알고 싶은 단을 입력 받고 해당 단을 출력해 주세요.
# # - input()
# # - 특정 단의 구구단을 출력 => 반복문 사용하기
# # --------------------------------------------------------
# num = int(input("원하는 구구단 단 수를 입력하세요(예: 3):"))
#
# if num:
#     if 2<=num<=9:
#         for multi in range(1,10):
#             print(f'{num} * {multi} =  {num * multi}')
#     else:
#         print("올바른 단 수를 입력해주세요.")
# else:
#     print("올바른 단 수를 입력해주세요.")
#
# # 내가 만든 것 - space 입력하면 에러뜨는 문제

# --------------------------------------------------------

# dan = input("좋아하는 단 입력:")
# if dan:
#     if dan.isdecimal():
#         dan=int(dan)
#         for num in range(1,10):
#             print(f'{dan} * {num} = {dan *num}')
#     else:
#         print("숫자만 입력 가능합니다.")
# else:
#     print("입력된 데이터가 없습니다.")
#
# # 선생님 예시
#
# # --------------------------------------------------------
#
# if dan.decimal():
#     dan=int(dan)
#     for num in range(1,10):
#         print(f'{dan} * {num} = {dan * num}')
# else:
#     print("정확한 데이터가 아닙니다.")
#
# # --------------------------------------------------------
# # [실습 2] 2단~ 9단까지 모두 출력 하세요. 반복문 사용하기!!!
# # --------------------------------------------------------


for dan in range(2,10):
    print(f'----{(dan)}단---- ', end="\t")
print('')
for dan in range(1,10):
    for num in range(2,10):
        print(f'{num} * {dan} = {dan *num}', end="\t")
    print('')
print('')

# 들여쓰기를 안 해서 자꾸 실패한 것
# 내가 만든 것
# # --------------------------------------------------------

for num in range(1, 10):
    for dan in range(2, 10):
        if num:
            print(f'{dan} * {num} = {dan*num:<2}', end='\n' if dan==9 else'   ')
        else:
            print(f'---{dan:^4}단---', end='\n' if dan==9 else '   ')