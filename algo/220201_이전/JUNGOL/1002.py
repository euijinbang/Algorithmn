import sys
sys.stdin = open("input.txt")

n = int(input())
nums = list(map(int, input().split()))


# a, b 대소 무관
def get_gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


gcd = lcm = nums[0]

# 두 정수 a,b 의 최대공약수가 d 라면, 세 정수 a,b,c의 최대공약수는 d와 c의 최대공약수와 같다.
# 두 정수 a,b 의 최소공배수가 d 라면, 세 정수 a,b,c의 최소공배수는 d와 c의 최소공배수와 같다.
# 두 수의 곱은 두 수의 최대공약수와 최소공배수의 곱과 같다. => ??
for i in range(1, n):
    gcd = get_gcd(gcd, nums[i])
    lcm = lcm * nums[i] // get_gcd(lcm, nums[i]) # lcm = 최소공배수 x 새 정수 / 최소공배수와 새 정수의 최대공약수

print(gcd)
print(lcm)