def line(count=80, char='-'):
    """
    기능을 수행하고 돌려줄 값이 없으면 return 명령을 사용하지 않는다.
    """
    for i in range(0, count):
        print(char, sep='', end='')
    print()

line(17)


def is_even_number3(number):
    """
    리턴값 = 함수가 어떠한 기능을 수행하고 그 결과를 호출한 곳으로 돌려주는 값
    리턴은 한 번만 사용하는 것이 함수를 이해하기에 좋다
    """
    return False if number % 2 else True

def is_even_number4(number):
    return number % 2 == 0

