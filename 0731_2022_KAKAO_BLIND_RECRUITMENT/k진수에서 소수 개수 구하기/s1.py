def isPrime(num):
    if num == 1:
        return False
    # 루트n 까지 검사
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0

    # k 진수로 변환
    changed = ''
    a = n // k
    while a > 0:
        a, b = divmod(n, k)
        changed = str(b) + changed
        n = a

    # 0 기준으로 나누기
    nums = changed.split('0')
    for n in nums:
        if n and isPrime(int(n)):
            answer += 1

    return answer