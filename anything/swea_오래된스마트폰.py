import sys
sys.stdin = open("oldphone_input.txt")
"""
T : 테스트케이스 수
N : 터치 가능한 숫자의 개수
O : 터치 가능한 연산자 개수
M : 최대 터치 가능한 횟수
nums : 터치 가능한 숫자들
cals : 터치 가능한 연산자들
W : 원하는 숫자

구하는 것 : 원하는 숫자 W를 만들 수 있는 최소 터치 횟수
최대 터치 가능한 횟수 M 이내에 원하는 숫자 W를 만들 수 없는 경우 -1 출력

- 계산 도중 연산결과가 음수가 되거나 999를 넘어가면 안된다.
- 터치 가능한 숫자는 0~9 사이의 정수
- '='는 언제나 터치 가능하낟.
- 나누기 '/' 연산은 정수 부분만 취하며 0으로 나눠서는 안된다.
"""
T = int(input())

cal_list = {
    1: '+',
    2: '-',
    3: '*',
    4: '/'
}


def solution():
    pass


for tc in range(1, T + 1):
    N, O, M = map(int, input().split())
    nums = list(map(int, input().split()))
    cals = list(map(int, input().split()))
    W = int(input())

    solution()
    print("#{} {}".format(tc, answer))
