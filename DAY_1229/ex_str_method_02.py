# ----------------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드(Method) 살펴 보기
# - 메서드(Method)
#   특정 데이터 타입에서만 사용 가능한 함수를 의미
#   사용 방법
#   변수명.메서드명() ==> msg="Good"
#                     msg. 으로 검색 후
#                     msg.메서드명()
#   데이터.메서드명() ==> "Good".메서드명()
# ----------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index()
# - 왼쪽 ----> 오른쪽, 제일 먼저 발견되는 문자의 인덱스를 반환
# - 존재하지 않는 str 인덱스 찾을려고 하면 Error 발생
# ----------------------------------------------------------

data = "Merry Christmas"
#       012345678901234
#         23  6 8
print(f"data.index('C')) => {data.index('C')}")
print(f"data.index('r')) => {data.index('r')}")
print(f"data.index('r', 3)) => {data.index('r',3)}")
print(f"data.index('r', 4)) => {data.index('r',4)}")
print(f"data.index('r', {data.index('r')}+1) => {data.index('r')+1}")

first_r=data.index('r')                      # 0번 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
print(f"data.index('r', first_r+1) => {data.index('r'), first_r+1}")

second_r = data.index('r', first_r+1)  # 첫 번째 'r' 인덱스 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
third_r = data.index('r', second_r+1)  # 두 번째 'r' 인덱스 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기

# 하지만 이렇게 하는 것이 재사용하지 않기 때문에
# 그냥 data.index('r')를 넣는 것이 메모리 상 나은 편이긴 하나
# 알아보기 용이한 장점이 있음


# ----------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => find()
# - 왼쪽 ----> 오른쪽, 제일 먼저 발견되는 문자의 인덱스를 반환
# - 존재하지 않는 str 인덱스 찾을려고 하면 -1 발생 (0번부터는 이미 할당되어 있기 때문에)
# ----------------------------------------------------------

# !의 인덱스를 찾기
print(f"data.find('!')) => {data.find('!')}")

# ----------------------------------------------------------
# str 데이터에서 문자열 분리해주는 메서드 => split()
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str로 분리
# ----------------------------------------------------------

data = "Happy New Year 1 2 3 4 5"

# str에서 공백을 기준으로 str 나누기
datas = data.split()
print(f"datas => {datas}")
print( type( datas ), datas)
# print(datas[2:][:4][1:]) 슬라이싱을 반복하면 왼쪽부터 슬라이싱 된 내용을 처리한 후 다시 리스트 상태에서 슬라이싱 함

# list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
print( f" datas[0] => {datas[0]}")
print( f" datas[1] => {datas[1]}")
print( f" datas[-1] => {datas[-1]}")
print(f"datas => {data.split('e')}")

juminNo = '123456-1234567'
birth = juminNo[:juminNo.index('-')]
number = juminNo[juminNo.index('-')+2:]
juminNos = juminNo.split('-')
print(juminNos)