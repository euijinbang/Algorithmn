# 최대공약수 GCD
# 최소공배수 LCM

# def gcd_get(a, b):
#     GCD = 1
#     for i in range(1, 10001):
#         if a % i == 0 and b % i == 0:
#             if i > GCD:
#                 GCD = i
#
#     aa = a // GCD
#     bb = b // GCD
#
#     print(GCD)
#     print(aa * bb * GCD)


# 유클리드 호제법
# A를 B로 나눈 나머지가 r이라면 A와 B의 최대공약수는 B와 r의 최대공약수와 같다.
# GCD(30, 18) = GCD(18, 12) = GCD(12, 6)
# 즉, 30과 18의 최대공약수는 12와 6의 최대공약수와 같다.

# a, b = map(int, input().split())
def gcd_get(a, b):
    while b != 0:
        r = a % b   # 나머지를 구한 후 a를 b로, b를 r로 바꾸고 반복한다.
        a = b
        b = r
    return a # b가 0이면 a가 최대공약수이므로 종료한다.

print(gcd_get(a, b))

# 두 수의 곱은 두 수의 최대공약수와 최소공배수의 곱과 같다.
lcd = a * b // gcd_get(a, b)
print(lcd)
