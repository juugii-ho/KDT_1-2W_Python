# for i in range(1, 101):
#     print(i)
#
# for i in range(1, 101):
#     if i % 3== 0:
#         print('Fizz')
#     elif i% 5 ==0:
#         print('Buzz')
#     else:
#         print(i)
#
# for i in range(1, 101):
#     if i & 3 == 0 and i % 5 ==0:
#         print('FizzBuzz')
#     elif i % 3 ==0:
#         print('Fizz')
#     elif i % 5 ==0:
#         print('Buzz')
#     else:
#         print(i)
#
# # if i % 3 == 0:
# #     print('Fizz')
# # elif i % 5 ==0:
# #     print('Buzz')
# # elif i % 3==0 and i % 5 ==0:      #FizzBuzz 검증이 안 됨
# #     priint('FizzBuzz')
# # else:
# #     print(i)
#
# for i in range(1,101) :
#     if i % 15 ==0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
#
# for i in range(1,101):
#     print('Fizz' * (i%3 ==0) + 'Buzz' * (i%5==0) or i)
#
# print('Fizz'+'Buzz')
# print('Fizz'*True)
# print('Fizz'*False)
#
# print('Fizz'*(i%3==0))
# print('Buzz'*(i%5==0))
# print('Fizz' * (i%3 ==0) + 'Buzz' * (i%5==0))
#
# print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)


min, max = input().split()
min = int(min)
max = int(max)
for data in range(min, max+1):
    if min%5==0 and min%7==0 :
       print('FizzBuzz')
    elif min%5==0:
        print('Fizz')
    elif min%7==0:
        print('Buzz')
    else:
        print(min)
    min +=1
