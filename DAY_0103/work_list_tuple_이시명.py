
a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

a = []
a.append(10)
print(a)

a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(2,500)
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(0, 500)
print(a)

a = [10, 20, 30]
a.insert(1,[500, 600])
print(a)

a = [10, 20, 30]
print(a.pop())
print(a)

a = [10, 20, 30]
del a[1]
print(a)

a = [10, 20, 30]
a.remove(20)
print(a)

a = [10, 20, 30, 20]
a.remove(20)
print(a)

a = [10, 20, 30, 15, 20, 40]
print(a.index(20))
print(a.count(20))
a.reverse()
print(a) #print(a.reverse())는 None 나옴

a = [10, 20, 30]
a.clear()
print(a)

a= [10, 20, 30]
del a[:]
print(a)

a = [10, 20, 30]
a[len(a):] = [500]
print(a)

a = [10, 20, 30]
a[len(a):] = [500, 600]
print(a)

seq = [10, 20, 30]
print(seq[-1])

seq = []
if seq:
    print(seq[-1])

a = [0,0,0,0,0]
b = a

print(a is b)

b[2] = 99
print(a)
print(b)

a = [0,0,0,0,0]
b = a.copy()

print(a is b)

print(a == b)

b[2] = 99
print(a)
print(b)

a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

for i in [38,21,53,62,19]:
    print(i)

for index, value in enumerate(a):
    print(index+1, value)

for index, value in enumerate(a, start=1):
    print(index, value)

a= [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)


a= [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(largest)


a= [38, 21, 53, 62, 19]
a.sort()
print(a[0])
a.sort(reverse=True)
print(a[0])

a = [10, 10, 10, 10, 10]
print(sum(a))

a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(10)]
print(c)
d = [i*2 for i in range(10)]
print(d)

a = [i for i in range(10) if i % 2 ==0]
print(a)

b = [i + 5 for i in range(10) if i % 2 == 1]
print(b)

a = [i*j for j in range(2,10) for i in range(1,10) ]
print(a)

a = [i * j for j in range(2,10)
          for i in range(1,10)]
print(a)


a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = list(map(str, range(10)))
print(a)

# a = input().split()
# print(a)

a,b =[10, 20]
print(a)
print(b)
#
# a,b = map(int, input().split()) 를 풀어서 쓰면
#
# x = input().split()
# m = map(int, x)
# a,b = m

a = (38, 21, 53, 62, 19, 53)
print(a.index(53))

a = (10, 20, 30, 15, 20, 40)
print(a.count(20))

a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end=' ')
print()

a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

print(i for i in range(10) if i % 2 == 0)

a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))




a,b = input().split(' ')
jegob3 = []
for jegob in range(int(a),int(b)+1):
    if jegob == int(b):
        jegob3.append(2**jegob)
    else:
        jegob3.append(2**jegob)
jegob3.pop(-2)
jegob3.pop(2)
print(jegob3)