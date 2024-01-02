# ------------------------------------------------------------
# List의 원소/요소 데이터 변경 및 삭제
# ------------------------------------------------------------
# "Merry Christmas"의 문자 1개 1개를 원소로 가지는 리스트로 생성하기

MC = list("Merry Christmas")
print(f'MC => {MC}')

# => ' ' 데이터를 '***'로 변경하기
# MC_space = MC[5]
print(f'MC[5] => {MC[5]}')
MC[5] = '***'
print(f'MC[5] => {MC[5]}')
print(f'MC => {MC}')        #list는 각 문자마다 코드값이 있기 때문에 부분 할당이 가능함

# 삭제(명령어임, 함수X) ==> del 데이터 또는 del(데이터)--------------------
del MC[5]
print(f'MC[5] => {MC[5]}')
print(f'MC => {MC}')

del (MC[5])
print(f'MC[5] => {MC[5]}')
print(f'MC => {MC}')

del MC
# print(MC)