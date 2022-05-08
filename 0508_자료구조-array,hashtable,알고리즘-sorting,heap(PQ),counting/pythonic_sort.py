"""
python style sorting 구현
"""
# 문제: [1] descending => [2] ascending 순서로 정렬하기
data = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

# 방법1. 문자열은 -x[1] 못쓰니까.. 다른거에 - 붙이고, reverse=True 주면 된다
s = sorted(data, key=lambda x: (x[1], -x[2]), reverse=True)

# 방법2. [2]를 먼저 정렬하고, [1]에 reverse를 주어 정렬하면 [2] 순서가 유지된다.
s = sorted(data, key=lambda x: x[2])
sorted(s, key=lambda x: x[1], reverse=True)
