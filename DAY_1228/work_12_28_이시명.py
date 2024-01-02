'''
1. 아래에 데이터를 저장하는 코드를 작성하세요:
'''

q1 = "kim1234@naver.com"
q2 = "http:www.naver.com"
q3 = "홍길동"
q4 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr"
q5 = "ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ"
q6 = "881120-1068234"

print(f'1-1 : ', q1[:7])
print(f'1-2 : ', q2[9:])
print(f'1-3 : ', q3[1:])
print(f'1-4 : 대문자 -', q4[::2], ', 소문자 -', q4[1::2])
print(f'1-5 : ', q5[3::4])
print(f'1-6 : 생년월일 -', q6[:6], ', 숫자부분 -', q6[7:])

'''
2. 아래 조건에 만족하도록 코드 작성하세요.
'''

input_int = int(input('정수 입력 :'))
print(f'''10진수 {input_int}
16진수 : {hex(input_int)}
 8진수 : {oct(input_int)}
 2진수 : {bin(input_int)}''')

'''
3. 아래 조건에 만족하도록 코드 작성하세요.
'''

input1 = input('Happy를 입력하세요: ')
input2 = input('New를 입력하세요: ')
input3 = input('Zoo를 입력하세요: ')

print(f'''코드 값이 가장   큰 단어 : {max(input1,input2,input3)}
코드 값이 가장 작은 단어 : {min(input1,input2,input3)}''')

'''
4. 아래 조건에 만족하도록 코드 작성하세요.
# '''
sentence = "오늘은 행복한 Thursday입니다."
input4 = input('목요일을 입력하세요: ')
print(f"'{input4}' 단어 메시지 존재 여부 : {bool(input4 in sentence)}")

input5 = input('happy를 입력하세요: ')
print(f"'{input5}' 단어 메시지 존재 여부 : {bool(input5 in sentence)}")

'''
5. 아래 조건에 만족하도록 코드 작성하세요.
'''
input6 = input('Zoo를 입력하세요: ')
print(f'{input6} 코드값 : {bin(ord(input6[0]))[2:]} {bin(ord(input6[1]))[2:]} {bin(ord(input6[2]))[2:]}' )