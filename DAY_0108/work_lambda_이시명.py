# 32
# 32.1

def plus_ten(x):
    return x + 10
print(plus_ten(1))

print(lambda x : x+10) #<function <lambda> at 0x1030e4280>

plus_ten = lambda x: x +10
print(plus_ten(1))

print((lambda x: x +10)(1))

# print((lambda x: y  = 10; x +y)(1)) #SyntaxError: invalid syntax

y = 10
print((lambda x : x+y)(1))  # 변수 선언은 lambda 외부에서 선언

def plus_ten(x):
    return x + 10

print(list(map(plus_ten, [1,2,3])))

print(list(map(lambda x: x +10, [1,2,3])))
print((lambda  : 1)())
x = 10
print((lambda  : x)())


a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x%3 ==0 else x, a)))
# print(list(map(lambda x : str(x) if x % 3 ==0, a))) elif 불가능

a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
)

def f(x):
    if x ==1:
        return str(x)
    elif x ==2:
        return float(x)
    else:
        return x + 10
a = [1,2,3,4,5,6,7,8,9,10]
print(list(map(f,a)))

a=[1,2,3,4,5]
b=[2,4,6,8,10]
print(list(map(lambda  x, y: x*y, a,b)))

def f(x):
    return x >5 and x<10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f,a)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f,a)))

def f(x,y):
    return x + y
a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(f,a))

a = [1,2,3,4,5]
from functools import  reduce
print(reduce(lambda x, y : x+y, a))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print([i for i in a if i>5 and i <10])


a = [1,2,3,4,5]
x = a[0]
for i in range(len(a)-1):
    x = x + a[i +1]

print(x)