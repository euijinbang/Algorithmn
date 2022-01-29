"""
a > b 일 때, 두 양의 정수 a, b의 최대공약수를 구한다.
양의 정수 k, r은 a를 b로 나눈 나머지이다.
GCD(a, b) = GCD(b, r)

"""


def algorithmn_gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    while b != 0:
        r = a % b
        a = b
        b = r

    return a


print(algorithmn_gcd(165, 150))
