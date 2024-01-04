START = False

# 17
if START :
    i = 0
    while i < 100:
        print('Hello, world!')
        i += 1

    i = 0
    while i <100:
        print('Hello, world!')
        i += 1

    i = 1
    while i <= 100:
        print('Hello, world!', i)
        i += 1

    i = 100
    while i > 0:
        print('Hello, world!', i)
        i -= 1

    count = int(input('반복할 횟수를 입력하세요: '))

    i = 0
    while i < count:
        print('Hello world!', i)
        i += 1


#17.1.3

import random

print(random.random())

print(random.randint(1,6))

i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)

dice = [1, 2, 3, 4, 5, 6]
print(random.choice(dice))
print(random.choice(dice))
print(random.choice(dice))

# while 1:
#     print('Hello, world!')
# while 'Hello':
#     print('Hello, world!')

num = 1350
inp = int(input())
while inp>=1350:
    print(f'{inp-num}')
    inp -= num
