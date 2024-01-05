# print('Hello, world!'.replace('world', 'Python'))
#
# s = 'Hello, world!'
# s = s.replace('world!', 'Python!')
# print(s)
#
# table = str.maketrans('aeiou', '12345')
# print('apple'.translate(table))
#
# print('apple pear grape pineaplle orange'.split())
# print('apple, pear, grape, pineapple, orange'.split(', '))
#
# print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
#
# print('python'.upper())
# print('PYTHON'.lower())
#
# print('    Python    '.lstrip())
# print('    Python    '.rstrip())
# print('    Python    '.strip())
#
# print(',python.'.lstrip(',.'))
# print(',python.'.rstrip(',.'))
# # print('가나다라마바사').lstrip('가다마사') str은 안되는듯?
#
# print('python'.ljust(10)) # 총 10칸을 지정해서 남는 공간을 공백으로
# print('python'.rjust(10))
# print('python'.center(10))
# print('python'.center(11)) # 홀수로 남으면 왼쪽에 한 칸 더
#
# print('python'.rjust(10).upper())
#
# print('35'.zfill(4))        # 0035
# print('3.5'.zfill(6))       # 0003.5
# print('hello'.zfill(10))    # 00000hello
#
# print('apple pineapple'.find('pl'))     # 2  // 0,1,2 자리
# print('apple pineapple'.find('xy'))     # -1 // 없으면 -1
#
# print('apple pineapple'.rfind('pl'))    # 12 // 오른쪽부터 찾기
# print('apple pineapple'.rfind('xy'))    # -1
#
# print('apple pineapple'.index('pl'))    # 2 // find랑 같지만 에러가 발생
#
# print('apple pineapple'.rindex('pl'))   # 12 // 오른쪽부터
#
#
# print('I am %s'%'james')    # %s str
#
# name = 'maria'
# print('I am %s'%name)
#
# print('I am %d years old' % 20)     # %d decimal
#
# print('%f'%2.3)         # 2.300000 % f float    기본 소수점 아래 6자리
# print('%.2f'%2.3)       # 2.30     %.2f         소수점아래 2자리
# print('%.3f'%2.3)       # 2.300    %.3f
#
# print('%10s' % 'python')    # '    python' %10s 10space?
#
# print('%10d' % 150)         # '       150'
# print('%10d' % 15000)       # '     15000'
# print('%10.2f'%2.3)         # '      2.30'  10자리 중 소수점 아래 2자리
# print('%10.2f'%2000.3)      # '   2000.30'
# print('%-10s'%'python')     # 'python    '  '-'하면 왼쪽 정렬
#
# print('Today is %d %s.' % (3, 'April'))
# # print('Today is %d %s.' % ('April', 3))  순서 바뀌면 안됨
#
# print('Today is %d%s.' % (3, 'April'))
#
# print('Hello, {0}'.format('world!'))    # Hello, world!
# print('Hello, {0}, {2}, {1}'.format('Python', 'Script', 3.6))
# # 순서에 맞게만 format 메서드 사용하면 됨
#
# print('{0} {0} {1} {1}'.format('Python', 'Script'))
#
# print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
# # 인덱스 생략하면 앞에서부터 순서대로 들어감
#
# print('Hello, {language} {version}'.format(language='Python', version=3.6))
# # 인덱스 이름으로도 가능
#
# language = 'Python'
# version = 3.6
# print(f'Hello, {language} {version}')
#
# print('{0:<10}'.format('python'))   # : + <or^or> + 총 칸 수
# print('{0:>10}'.format('python'))
# print('{:<10}'.format('python'))
#
# print('%03d' % 1)   # 공백에는 0을 넣는, 3칸짜리, 10진수
# print('{0:03d}'.format(35)) # 0 채워라/3자리/10진수/35넣기
# print('{0:03d}'.format(1))  # 0 채워라/3자리/10진수/1넣기
#
# print('%08.2f' % 3.6)       # 0 채워라/8자리/소수점 아래 2자리/3.6넣기
# print('{0:08.2f}'.format(150.37)) # 0채워라/8자리/소수점 아래 2자리/150.37 넣기
#
# print('{0:0<10}'.format(15))  # 1500000000 // 0 채워라/왼쪽정렬/10공간/15넣기
# print('{0:0>10}'.format(15))  # 0000000015 // 0 채워라/오른쪽정렬/10공간/15넣기
#
# print('{0: >10}'.format(15))  #'        15'//' '채워라/오른쪽정렬/10공간/15넣기
# print('{0:>10}'.format(15))   #'        15'//' '채워라/오른쪽정렬/10공간/15넣기
#                                     #         ㄴ default가 공백
# print('{0:x>10}'.format(15))  # xxxxxxxx15// x 채워라/오른쪽정렬/10공간/15넣기
#
# print(format(1493500, ','))   # 1,493,500 // 기본으로 천단위 콤마
# print('%20s'%format(1493500, ',')) # '           1,493,500' 전체 20칸/ 천단위 콤마
# print('{0:,}'.format(1493500))  # 천단위 콤마
# print('{0:>20,}'.format(1493500))   # 공백채워라/오른쪽정렬/ 20칸 / 천단위 콤마
# print('{0:0>20,}'.format(1493500))  # 0 채워라/오른쪽정렬/ 20칸 / 천단위 콤마

# a = input().split()
a2 = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
for b in a2:
    c = []
    b2 = b.index('the')
    c.append(b2)
print(c)