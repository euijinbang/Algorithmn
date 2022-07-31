def n_to_kth(n, k):
    """
    정수 n 을 k 진수로 변환
    """
    tmp = ''
    while n > 0:
        n, rest = divmod(n, k)
        tmp = str(rest) + tmp   # 나머지를 거꾸로 출력

    return tmp


def is_prime_num(n):
    """
    소수 찾기 : N-1 ~ 2 까지의 수 중, 어떠한 수로도 나누어지지 않는 수
    """
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(n, k):
    kth_number = n_to_kth(n, k)
    print(kth_number)
    numbers = kth_number.split('0')
    answer = 0
    for number in numbers:
        if number and is_prime_num(int(number)):  # 110011 split 시 공백 발생 ['11', '', '11']
            answer += 1

    return answer