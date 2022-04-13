N = int(input())
data = input().split()
M = int(input())
check = input().split()

hash_table = {}

for d in data:
    key = hash(d.encode())
    hash_table[key] = d

for c in check:
    key = hash(c.encode())
    # 1. key에러로 확인하는 방법
    # try:
    #     if hash_table[key]:
    #         print(1)
    # except:
    #     print(0)

    # 2. 키값 확인하는 방법
    if key in hash_table.keys():
        print(1)
    else:
        print(0)
