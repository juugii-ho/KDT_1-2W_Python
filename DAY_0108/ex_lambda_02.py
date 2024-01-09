# 리스트 안에 모든 원소를 더한 합계 출력
datas = ['1', '4', '9']
for idx, d in enumerate(datas):
    datas[idx] = int(d)

print(datas)

# => 내장함수 map()
print(list(map(int, datas)))
print(list(map(float, datas)))

# => 원소에 *100한 값을 리스트에 저장하기
def multiValue(x):
    return x*100

print(list(map(multiValue, datas)))

datas = list(map(lambda x : x*100, datas))
print(datas)

def greeting():
    print("반갑습니다.~")
greeting()

print( ( lambda: "반갑습니다.")())