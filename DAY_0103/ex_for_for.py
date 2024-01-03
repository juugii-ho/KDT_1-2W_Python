# 1 ~ 10 출력 ---------------------------------------------------
# 방법 1
print(1)
print(2)
# ...
print(10)
print("")

# 방법 2 + 홀수 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in nums:
    if n>0:
        print(n)
        if n%2:
            print("홀수")     #for문 빠져나올 때까지 수행

print("")

for a in range(1,11):
    print(a, end=' ' if a != 5 else '\n') # 1 2 3 4 5 \n 6 7 8 9 10
print("END")                #for문 빠져나오고 출력

max = 5
for a in range(1,max):
    print(f'{"*"*a :^{max}}')
for a in range(max,0,-1):
    print(f'{"*"*a :^{max}}')