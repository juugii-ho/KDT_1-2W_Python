# # i = 0
# # while True:
# #     print(i)
# #     i += 1
# #     if i == 100:
# #         break
# #
# # for i in range(10000):
# #     print(i)
# #     if i == 100:
# #         break
# #
# # for i in range(100):
# #     if i % 2 == 0:
# #         continue
# #     print(i)
# # for i in range(10):
# #     pass
# #
# # while True:
# #     pass
# #
#
# count = int(input('반복할 횟수를 입력하세요: '))
#
# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == count:
#         break
#
# count = int(input('반복할 횟수를 입력하세요: '))
#
# for i in range(count+1):
#     if i % 2 == 0:
#         continue
#     print(i)

start, stop = map(int, input().split())

i = start

while True :
    j = stop
    if i == j:
        break
    if i%10==3:
        i +=1
        continue
    print(i, end=' ')
    i += 1