arr = [x+1 for x in range(20)]

arr = list(map(int, input().split()))
new_arr = []

for i in range(len(arr)):
    if i % 3 == 2:
        new_arr.append(str(arr[i]))

print(new_arr)