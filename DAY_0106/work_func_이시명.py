def hello():
    print('Hello, world!')

hello()

def hello():
    pass

hello()

def add(a, b):
    print(a + b)

add(10, 20)


def add(a, b):
    '''독스트링'''
    return a + b
x = add(10,20)
print(x)
print(add.__doc__)

def add(a, b):
    return a + b

x = add(10, 20)
print(x)
print(add(10,20))

def one():
    return 1

x = one()
print(x)

def not_ten(a):
    if a == 10:
        return
    print(a, '입니다.', sep='')

not_ten(5)
not_ten(10)

def add_sub(a, b):
    return a + b, a - b

x, y = add_sub(10, 20)
print(x)
print(y)

x = add_sub(10,20)
print(x)

x, y  = 30, -10
print(x)
print(y)

def one_two():
    return (1,2)

print(1, 2)

def one_two():
    return 1,2
def one_two():
    return [1,2]

x, y = one_two()
print(x, y)

def mul(a,b):
    c = a * b
    return c
def add(a, b):
    c = a+b
    print(c)
    d = mul(a,b)
    print(d)

x = 10
y = 20
add( x,y )


x, y = 40, 8

def calc(a, b):
    return a+b, a-b, a*b, a/b


a, s, m, d = calc(x,y)
print('{0}, {1}, {2}, {3}'.format(a,s,m,d))