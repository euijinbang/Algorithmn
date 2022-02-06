"""
1부터 Num 까지의 곱을 출력
"""


def multiple(data):
    ans = 1
    for i in range(2, data+1):
        ans = ans * i

    return ans


def multiple_recursive(data):
    if data == 1:
        return data
    else:
        return data * multiple_recursive(data-1)


"""
리스트의 합 구하기 (0 ~ 99)
"""
import random
data = random.sample(range(100), 10)


def sum_list(data):
    sum = 0
    for i in data:
        sum += i

    return sum


def sum_list_recursive(data):
    if len(data) == 1:
        return data[0]
    else:
        return data.pop() + sum_list_recursive(data)


"""
palindrome
"""


def is_palindrome_even_odd(data):
    if len(data) == 1:
        return True

    if len(data) % 2:
        if data[:len(data) // 2] == data[len(data) // 2 + 1:][::-1]:
            return True

    else:
        if data[:len(data) // 2] == data[len(data) // 2:][::-1]:
            return True
        
    return False


def is_palindrome_odd(data):
    if data[:len(data)//2] == data[len(data)//2+1:][::-1]:
        return True

    else:
        return False


def is_palindrome_recursive(data):
    if len(data) == 1:
        return True

    if data[0] == data[-1]:
        return is_palindrome_recursive(data[1:-1])
    else:
        return False


"""
정수 n 이 1이 될 될 때 까지 연산 과정을 출력
홀수면 3 * n + 1
짝수면 n // 2
"""


def sol(n):
    print(n)
    while n > 1:
        if n % 2:
            n = 3 * n + 1
            print(n)
        else:
            n = n // 2
            print(n)


def sol_recur(n):
    print(n)
    if n == 1:
        return 1

    if n % 2:
        return sol_recur(3 * n + 1)
    else:
        return sol_recur(n // 2)


"""
정수 n이 주어질 때, 
n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수
# f(n) = f(n-3) + f(n-2) + f(n-1)
"""


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return f(n-3) + f(n-2) + f(n-1)

