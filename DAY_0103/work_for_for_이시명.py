
# 19

for i in range(5):
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print('i:', i, '\\n', sep='')

for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

for i in range(3):
    for j in range(7):
        print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j ==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print("end")
#
# inp = int(input())
# inp2 = inp*2+1
# for i in range(inp2):
#     if i%2 == 0:
#         inp2 = inp2 -1
#         i = i -1
#     else:
#         print(' '*(inp2//2), end='')
#         print('*'*i, end='')
#         print(' '*(inp2//2), end='')
#         print()
#         inp2 = inp2 - 1
#         i = i +1

