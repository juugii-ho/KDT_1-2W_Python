# ------------------------------------------------------------
# 함수 안에 함수 정의 및 호출
# ------------------------------------------------------------
def print_hello():
    hello = "hello~!"

    def print_message():
        msg = hello + " ^^ "
        print(msg)

    print_message()
    # print(msg) 지역변수 사용 불가

# 함수 호출 ------------------------------------------------------------
print_hello()
# print_message() 접근이 안됨


def ff():
    x= 100
    def a():
        x=10                # 함수 a의 지역변수 x
        def b():
            nonlocal x
            x=20            # 함수 b의 지역변수 x

        b()
        print(x)

    a()
ff()




def foo():
    x = 10
    def test():       # test의 값으로 ( (값 10의 주소를 가진)지역변수 x의 주소)를 저장
        return x
    return test       # foo의 값으로 (test의 값인 ((값 10의 주소를 가진)지역변수 x)의 주소)를 반환

x = foo()
print(x())      # 지역변수 값을 보겠다

# 클로저를 사용하는 이유 : 지역변수에서 계속 사용하고 싶으나 전역변수로 노출하면 변경가능성이 있기 때문에 사용

