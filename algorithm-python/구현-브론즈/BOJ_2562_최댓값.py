arr = []
for i in range(9):
    arr.append(int(input()))

max_data = arr[0]
num = 0

for i in range(9):
    if arr[i] >= max_data:
        max_data = arr[i]
        num = i

print(max_data)
print(num+1)

