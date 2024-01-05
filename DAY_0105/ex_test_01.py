# -----------------------------------------------------------------
# [실습1] 2개의 정수를 입력 받은 후 사칙 연산 수행 결과를 반환하는
#        기능의 함수를 정의해주세요.
#        함수이름 : fourCalc
#        매개변수 : n1, n2
#        변환결과 : 사칙 연산 결과
# -----------------------------------------------------------------

def fourCalc(n1, n2):
    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else '0으로 나눌 수 없음'


print(fourCalc(1, 0))
# -----------------------------------------------------------------
# [실습2] 문자열을 16진수 코드값으로 변환 후 반환하는 기능의 함수를 정의해주세요.
#        함수이름 : getCode
#        매개변수 : message
#        변환결과 : str
# -----------------------------------------------------------------

def getCode(message):
    # pass
    ret = ''
    for msg in message:
        ret += hex(ord(msg)) + ' '
    return ret

print(getCode(('Good Luck')))

# 헛된 노력의 흔적..

#
#     message.split()
#
#     message2 = map(ord, message)
#     for idx, msg in enumerate(message):
#         message[idx] = hex(msg)

# message = ("안녕하세요")
# print(ord("안"))

# message = "message"
# print(ord(message))
#
# print(hex(message))
#
# print("안녕하세요".split())
# print(map(ord, "안녕하세요".split()
# print(list(map(int, "안녕하세요".split())))