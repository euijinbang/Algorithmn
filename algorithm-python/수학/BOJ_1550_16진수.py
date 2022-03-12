"""
16진법 : 16개의 수로 표현
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F
"""

info = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

# 16진수를 10진수로 변환해보자
# 2AC 라면 (2 * 16^2) + (A * 16^1) + (C * 16^0)
# num = '2AC'
num = input()
total = 0
num_list = list(num)[::-1]  # ['C', 'A', '2']


for i in range(len(num_list)):  # 인덱스 0, 1, 2, ...
    if num_list[i] in info.keys():
        total += info[num_list[i]] * (16 ** i)
    else:
        total += int(num_list[i]) * (16 ** i)

print(total)

# (추가) 10진수를 16진수로 변환해보자
num2 = 684

total2 = []
while num2 > 16:
    q = num2 // 16
    r = num2 % 16
    total2.append(r)
    num2 = q

total2.append(num2)  # [12, 10, 2]
result = ''

for v in total2[::-1]:  # 리스트 거꾸로 검사
    flag = False
    for key, value in info.items():
        if v == value:
            result += key
            flag = True

    if not flag:    # 키밸류쌍 통과 안했다면(A~F가 아니라면) 숫자를 더한다.
        result += str(v)

print(result)
