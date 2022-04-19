from itertools import combinations
# GCD: 최대공약수(유클리드 알고리즘)
# 조합구하기

# 모든 조합 쌍 구해서 a > b일 때마다 GCD 실행

# n = 3
# arr = [7, 5, 12]
# arr.sort(reverse=True)

# 라이브러리 활용
# arr2 = [7, 5, 12]
# print(list(combinations(arr2, 2)))

t = int(input())
for _ in range(t):
    n, *arr = map(int, input().split())  # n 과 그 뒤의 수는 리스트로 받기
    arr.sort(reverse=True)

    total = 0
    for i in range(n-1):
        for j in range(i+1, n):
            a, b = arr[i], arr[j]
            # print((a, b))
            # 유클리드 알고리즘
            if a >= b:
                val, r = divmod(a, b)
                while r != 0:   # 나머지가 0이면 종료
                    a = b
                    b = r
                    val, r = divmod(a, b)
                total += b

    print(total)


