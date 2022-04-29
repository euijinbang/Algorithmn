tree = [-1, 'A', 'B', 'C', 'D', '0', 'F', 'G', 'H', 'I', '0', '0']

#1. 트리높이 구하기 - 인덱스를 2의 제곱수로 올려가면서 높이찾기
height = 0
i = 1
while i < len(tree):
    if tree[i]:
        height += 1
        i = 2 ** height

print(height)

#2. leaf부터 부모까지 토너먼트 이기는 횟수 구하기
count = 0
start = 8
for i in range(len(tree)):
    if tree[start + 1] != '0':
        count += 1
    parent = start // 2
    start = parent

    if parent == 1:
        break

print(count)

#3. Lg cns 토너먼트 문제
# matches = [-1, 0, 0, 1, 2, 2, 3, 3, 4, 5, 5]
# m = 6
# opp = 9




