# --------------------------------------------------------
# 출력되는 문자열 str에서 형식/양식/서식 설정
# - 데이터 출력되는 칸 수, 정렬방향(왼쪽, 오르쪽, 가운데), 빈 칸 수 채우기
# --------------------------------------------------------
count = 1
print(f'파일명 : img_{count}.jpg') # 파일명 : img_1.jpg

count = 21
print(f'파일명 : img_{count}.jpg') # 파일명 : img_21.jpg

count = 101
print(f'파일명 : img_{count}.jpg') # 파일명 : img_101.jpg
# ----------------------------------
count = 1
print(f'파일명 : img_{count:3}.jpg') # 파일명 : img_  1.jpg

count = 21
print(f'파일명 : img_{count:3}.jpg') # 파일명 : img_ 21.jpg

count = 101
print(f'파일명 : img_{count:3}.jpg') # 파일명 : img_101.jpg
# ----------------------------------
count = 1
print(f'파일명 : img_{count:<3}.jpg') # 파일명 : img_1  .jpg

count = 21
print(f'파일명 : img_{count:<3}.jpg') # 파일명 : img_21 .jpg

count = 101
print(f'파일명 : img_{count:<3}.jpg') # 파일명 : img_101.jpg
# ----------------------------------
count = 1
print(f'파일명 : img_{count:0>3}.jpg') # 파일명 : img_001.jpg
#                   채울값/정렬방향/칸 수
count = 21
print(f'파일명 : img_{count:0>3}.jpg') # 파일명 : img_021.jpg
#                    ㄴ 변수는 count만 가능 '3' 같은 경우 못 바꿈
count = 101
print(f'파일명 : img_{count:0>3}.jpg') # 파일명 : img_101.jpg

count = 1001
print(f'파일명 : img_{count:0>3}.jpg') # 파일명 : img_1001.jpg
#칸 수 초과하면 무시하고 그냥 실행 됨
# ----------------------------------
count = 1
print(f'파일명 : img_{count:0^3}.jpg') # 파일명 : img_010.jpg
#                        가운데 정렬
count = 21
print(f'파일명 : img_{count:0^3}.jpg') # 파일명 : img_210.jpg
#                                 가운데 정렬 시 왼쪽 우선인 듯?
count = 101
print(f'파일명 : img_{count:0^3}.jpg') # 파일명 : img_101.jpg

avg = 98.1234
print(f'학급 평균: {avg:4}점') # 칸 수 초과하므로 다 나옴

avg = 98.1234
print(f'학급 평균: {avg:.2}점') # 앞에서부터 2자리 즉 98인데 지수표기로 나옴
# 학급 평균: 9.8e+01점
avg = 98.1234
print(f'학급 평균: {avg:.4}점') # 앞에서부터 4자리
# 학급 평균: 98.12점

print('학급 평균: %-7.2f점' %avg)
#              %와 알파벳 사이에 숫자
#           + 왼쪽 정렬 / - 오르쪽 정렬
#           정수 위치의 숫자는 표시할 자리 수
#        소수 위치의 숫자는 표시할 수가 몇자리까지인지