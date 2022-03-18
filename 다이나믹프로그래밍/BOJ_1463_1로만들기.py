"""
DP

초기값 
f(1) = 0

점화식
f(n) = f(n-1) + 1
f(n) = f(n//2) + 1
f(n) = f(n//3) + 1
"""

# N = int(input())


def dp(N):
    min_count = [0] * (N + 1)
    min_count[1] = 0    # 1이 가장 작은 문제. 1 일때의 연산 수는 0이다.
    
    """
    2, 3, 4, ..., 10 계산을 진행하며 더 작은 값을 담는다.
    f(2) = f(2-1)+1 또는 f(2//2)+1 중 더 작은 값
    f(3) = f(3-1)+1 또는 f(3//3)+1 중 더 작은 값
    f(4) = f(4-1)+1 또는 f(4//2)+1 중 더 작은 값
    ...
    f(10) = f(10-1)+1 또는 f(10//2)+1 중 더 작은 값
    
    최종적으로 최소 연산의 수가 배열에 담기므로 배열의 10번 인덱스 값을 출력하면 된다.
    """
    for i in range(2, N + 1):

        min_count[i] = min_count[i - 1] + 1    

        if i % 2 == 0:
            min_count[i] = min(min_count[i], min_count[i // 2] + 1)

        if i % 3 == 0:
            min_count[i] = min(min_count[i], min_count[i // 3] + 1)

    print(min_count)
    return min_count[N]


print(dp(5))
