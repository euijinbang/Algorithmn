arr = [x+1 for x in range(15)]

n = int(input())

partial_list = []

for i in arr:
    if i % n == 0:
        partial_list.append(i)

print(partial_list)

