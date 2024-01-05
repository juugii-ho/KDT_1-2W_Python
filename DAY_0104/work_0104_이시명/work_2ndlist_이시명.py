# a=[[10,20], [30,40], [50,60]]
# print(a)
#
# a= [[10, 20],
#     [30, 40],
#     [50, 60]]
# print(a)
#
# a=[[10,20], [30,40], [50,60]]
# print(a[0][0])
# print(a[1][1])
# print(a[2][1])
# a[0][1]=1000
# print(a[0][1])
# print(a)
#
# a = [[10, 20],
#      [500, 600, 700],
#      [9],
#      [30],[40],
#      [8],
#      [800, 900, 1000]]
# print(a)
#
# a=[]
# a.append([])
# a[0].append(10)
# a[0].append(20)
# a.append([])
# a[1].append(500)
# a[1].append(600)
# a[1].append(700)
# print(a)
#
# a= ((10, 20), (30, 40), (50,60))
# b= ([10, 20], [30, 40], [50, 60])
# c= [(10, 20), (30, 40), (50, 60)]
# print(a,b,c)
# # a[0][0]=500
# # a[0]=(500,600)
# b[0][0]=500
# # b[0]=(500,600)
# # c[0][0]=500
# c[0]=(500, 600)
# print(a, b, c)
#
# a = [[10,20], [30,40], [50,60]]
# print(a)
#
# from pprint import pprint
# pprint(a, indent=4, width=20)
#
#
# a = [[10,20], [30,40],[50,60]]
# for x, y in a:
#     print(x, y)
#
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()
#
# # for i in range(len(a)):
# #     for j in range(len(a)):
#         # print(a[i][j], end=' ')
#
# i = 0
# while i < len(a):
#     x, y = a[i]
#     print(x,y)
#     i += 1
#
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         print(a[i][j], end=' ')
#         j += 1
#     print()
#     i += 1
#
# # i = 0
# # while i < len(a):
# #     j = 0
# #     while j < len(a[i]):
# #         print(a[i][j], end=' ')
# #         j += 1
# #         i += 1
# #     print()
#
# a = []
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
# print(a)
#
#
# a = [[0 for j in range(2)] for i in range(3)]
# print(a)
#
# a = [3, 1, 3, 2, 5]
# b = []
#
# for i in a:
#     line = []
#     for j in range(i):
#         line.append(0)
#     b.append(line)
# print(b)
#
#
# students = [
#     ['john', 'C', 19],
#     ['maria', 'A', 25],
#     ['andrew', 'B', 7]
# ]
# print(sorted(students, key=lambda student: student[1]))
# print(sorted(students, key=lambda student: student[2]))
#
# a = [[10,20], [30,40]]
# b = a
# b[0][0] = 500
# print(a)
# print(b)
#
# a = [[10,20], [30,40]]
# b = a.copy()
# b[0][0] = 500
# print(a)
# print(b)
#
# a = [[10,20], [30,40]]
# import copy
# b = copy.deepcopy(a)
# b[0][0] = 500
# print(a)
# print(b)

#


col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

