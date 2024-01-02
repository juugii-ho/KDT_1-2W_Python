# 1. 아래에 데이터를 저장하는 코드를 작성하세요.
hometown = "대구"
blooddtype = "B"
season = "봄"
height = 172
callnumber = "010-5199-0181"
nation = "korea"

print('2. 화면출력 되도록 코드 작성하세요.')
mbti = 'INFP'
blood = 'A'
gender = 'M'
height = 171.7
weight = 77

#[출력] ---------------------------------------------------------------------------------------
#[ 신상 정보 ]
#MBTI : INFP 혈액형 : A 성별 : M
#몸무게 : 77 키 : 171.7
#[코드] ---------------------------------------------------------------------------------------
#① 여러데이터 출력 방식
print('[ 신상 정보 ]')
print('MBTI :', mbti, '혈액형 :', blood, '성별 :', gender)
print('몸무게 :', weight, '키 :', height)

# ② 서식지정자 출력 방식
print('[ 신상 정보 ]')
print('MBTI : %s 혈액형 : %s 성별 : %s'%(mbti, blood, gender))
print('몸무게 : %d 키 : %f'%(weight, height))

# ③ F-스트링 출력 방식

print(f'''[ 신상 정보 ]
MBTI : {mbti} 혈액형 : {blood} 성별 : {gender}
몸무게 : {weight} 키 : {height} ''')

print('3. 아래 내용에 맞도록 코드 작성해 주세요.')
print(f'데이터 50 => {type(50)}타입)
print(f'데이터 0.91 => {type(0.91)})
print(f'데이터 Winter => {type('Winter')})
print(type(False))

season1 = input("좋아하는 계절은? ")
print(f'당신은 {season}을 좋아하는 군요!')

season2 = input("봄은 영어로? ")
print(f'봄은 {season2}입니다.')

print('''4. 파이썬에서 메모리와 프로그램 코드와 관계입니다.
  빈칸에 해당하는 메모리 영역 이름을 적으세요.
- 힙 영역
- 스택 영역''')

print('''5. 아래에 요청하는 내용을 작성하세요.
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>''')

'''
[질문] 직육면체 가로길이(cm) : 10
[질문] 직육면체 세로길이(cm) : 10
[질문] 직육면체 높이길이(cm) : 3
[결과] 직사각형 넓이 : OOO
직사각형 부피 : OOO
'''
print('''6. 아래 내용에 맞도록 코드 작성해 주세요.
직육면체의 가로(cm), 세로(cm), 높이(cm)를 입력 받은 후 넓이/부피 출력하세요.''')
width = int(input('직육면체 가로길이(cm): '))
lenth = int(input('직육면체 세로길이(cm): '))
height = int(input('직육면체 높이길이(cm): '))
print('직사각형 넓이 :', width*lenth)
print('직육면체 부피 :', width*lenth*height)