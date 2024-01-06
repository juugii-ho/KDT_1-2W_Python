# # print(10, 20, 30)
# #
# # def print_numbers(a, b, c):
# #     print(a)
# #     print(b)
# #     print(c)
# #
# # print_numbers(10, 20, 30)
# #
# # x = [10, 20, 30]
# # print_numbers(*x)
# #
# # print_numbers(*[10,20,30])
# #
# # # print_numbers(*[10,20])
# #
# # def print_numbers(*args):
# #     for arg in args:
# #         print(arg)
# #
# # print_numbers(10)
# # print_numbers(10, 20, 30, 40)
# #
# # x = [10]
# # print_numbers(*x)
# # y = [10, 20, 30, 40]
# # print_numbers(*y)
# #
# # def print_numbers(a, *args):
# #     print(a)
# #     print(args)
# #
# # print_numbers(1)
# # print_numbers(1, 10, 20)
# # print_numbers(*[10, 20, 30])
# #
# def personal_info(name, age, address):
#     print('이름', name)
#     print('나이', age)
#     print('주소', address)
#
# #
# # print(personal_info('홍길동', 30, '서울시 용산구 이촌동'))
# #
# # print(personal_info(age= 30, address='서울시 용산구 이촌동', name = '홍길동'))
# #
# # print(10, 20, 30, sep=':', end='')
#
# # x = {'name':'홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# # print(personal_info(**x))
# # print(personal_info(**{'name':'홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}))
#
# # print(personal_info(**{'name':'홍길동', 'old': 30, 'address': '서울시 용산구 이촌동'}))
# # age => old
# # print(personal_info(**{'name':'홍길동', 'age': 30}))
# # address가 없음
#
# x = {'name':'홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# personal_info(*x)
# personal_info(**x)
#
#
# def personal_info(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw, ': ', arg, sep='')
#
# personal_info(name = '홍길동')
#
# x = {'name':'홍길동'}
# personal_info(**x)
# y = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}
# personal_info(**y)
#
# def personal_info(name, **kwargs):
#     print(name)
#     print(kwargs)
#
# personal_info('홍길동')
# personal_info('홍길동', arg=30, address='서울시 용산구 이촌동')
# personal_info(**{'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'})
#
# def custom_print(*args, **kwargs):
#     print(*args, **kwargs)
# custom_print(1,2,3, sep=':', end='')
#
# def personal_info(name, age, address='비공개'):
#     print('이름: ', name)
#     print('나이: ', age)
#     print('주소: ', address)
#
# personal_info('홍길동', 30)
#
# personal_info('홍길동', 30, '서울시 용산구 이촌동')
#
# # def personal_info(name, address='비공개', age) # 초깃값 지정은 뒤로
# #     print('이름: ', name)
# #     print('나이: ', age)
# #     print('주소: ', address)
#
# # def personal_info(name, age, address='비공개'):
# # def personal_info(name, age = 0, address='비공개'):
# # def personal_info(name='비공개', age=0, address='비공개'):
#
#
#
korean, english, mathematics, science = map(int, input().split())

def get_min_max_score(*data):
    return max(data), min(data)


def get_average(**data):
    return (sum(data.values()) / len(data))





min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

data = []
for d in data:
    data.append(d)
    max(d)