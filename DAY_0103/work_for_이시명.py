# 16

for i in range(100):
    print('Hello, world!')

print(range(10))
print(list(range(10)))

for i in range(5,12):
    print('Hello, world!', i)

for i in range(0, 10, 2):
    print('Hello, world!', i)

for i in range(10, 0):           #는 작동하지 않음 - 10에서 0개만 사용하기 때문
    print('Hello, world', i)

for i in range(10,0,-1):
    print('Hello, world!', i)

for i in reversed(range(10)):
    print('Hello, world!', i)

for i in range(10):
    print(i, end=' ')
    i = 10
print("")

# count = int(input('반복할 횟수를 입력하세요: '))

# for i in range(count):
#     print('Hello, world!', i)

a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)

for letter in 'Python':
    print(letter, end= ' ')
print("")

for letter in reversed('Python'):
    print(letter, end=' ')
print("")
#
# a = int(input())
# for num in range(1,10):
#     print(f'{a} * {num} = {a*num}')