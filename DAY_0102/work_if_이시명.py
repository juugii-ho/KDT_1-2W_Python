# # # 13.1
# # x = 10
# # if x ==10:
# #         print('10입니다.')
# #
# # # if x = 10: #SyntaxError: invalid syntax
# #
# # #if x == 10 SyntaxError: invalid syntax
# #
# #
# # # 13.2
# # x = 10
# # if x ==10:
# #     pass
# #
# # if x == 10:
# #     pass
# #
# # x = 10
# #
# # if x == 10:
# #     print('x에 들어있는 숫자는')
# #             # print('10입니다.') # IndentationError: unexpected indent
# #
# # # 13.3
# # x = 15
# # if x >= 10:
# #     print('10이상입니다.')
# #     if x ==15:
# #         print('15입니다.')
# #     if x ==20:
# #         print('20입니다.')
# #
# # # 13.4
# # x = int(input())
# #
# # if x ==10:
# #     print('10입니다.')
# # if x ==20:
# #     print('20입니다.')
# #
# # # 14.1
# #
# # x = 5
# # if x ==10:
# #     print('10입니다.')
# # else:
# #     print('10이 아닙니다.')
#
# x = 5
# if x ==10:
#     y = x
# else:
#     y = 0
# print(y)
#
# x = 5
# y = x if x == 10 else 0
# print(y)
#
# #14.2
#
# x = 5
# if x ==10:
#     print('10입니다.')
# else:
# # print('x에 들어있는 숫자는') #IndentationError: expected an indented block
#     print('10이 아닙니다.')
#
# x = 10
# if x == 10:
#     print('10입니다.')
# else:
#     print('x에 들어있는 숫자는')
# print('10이 아닙니다.') #출력되지 않아야 하는데 출력됨
#
# x =10
# if x ==10:
#     print('10입니다.')
# else:
#     print('x에 들어있는 숫자는')
#
# # print('10이 아닙니다.') #if 문에 속하지 않는 구절
#
# # 14.3
# if True:
#     print('참')
# else:
#     print('거짓')
#
# if False:
#     print('참')
# else:
#     print('거짓')
#
# if None:
#     print('참')
# else:
#     print('거짓')
#
# if 0:
#     print('참')
# else:
#     print('거짓')
#
# if 1:
#     print('참')
# else:
#     print('거짓')
#
#
# if 0x1F:
# # print(bin(0x1F)) #111111
#     print('참')
# else:
#     print('거짓')
#
# if 0b1000:
#     print('참')
# else:
#     print('거짓')
#
# if 13.5:
#     print('참')
# else:
#     print('거짓')
#
#
# if 'Hello':
#     print('참')
# else:
#     print('거짓')
#
# if '':
#     print('참')
# else:
#     print('거짓')
#
# if not 0:
#     print('참')
#
# if not None:
#     print('참')
#
# if not '':
#     print('참')
#
# x = 10
# y = 20
#
# if x == 10 and y == 20:
#     print('참')
# else:
#     print('거짓')
#
# if x>0:
#     if x < 20:
#         print('20보다 작은 양수입니다.')
#
# if x > 0 and x < 20:
#     print('20보다 작은 양수입니다.')
#
# if 0 < x < 20:
#     print('20보다 작은 양수입니다.')
#
#


#14. 6
#
# (korean, english, math, science) = input("점수를 입력하세요: ").split(" ")
#
# if 0<int(korean)<100 and 0<int(english)<100 and 0<int(math)<100 and 0<int(science)<100:
#     if (int(korean) + int(english) + int(math) + int(science)) / 4 >= 80:
#         print("합격")
#     else:
#         print("불합격")
# else:
#     print("잘못된 점수")

#---------------------------------------------------------

# 15.1

x = 20
if x ==10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')

x = 30

if x == 10:
    print('10입니다.')
elif x == 20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')
#
# if x ==10:
#     print('10입니다.')
# else:
#     print('10도 20도 아닙니다.')
# elif x ==20:
#     print('20입니다.')

button = int(input())

if button ==1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')


# 15.4
age = int(input())
balance = 9000
age1 = 650
age2 = 1050
age3 = 1250

if 7 <= age <= 12:
    print(f"{balance-age1}")
elif 13<= age <= 18:
    print(f"{balance-age2}")
else:
    print(f"{balance-age3}")