# arr = [18, -5, 10]

arr = list(map(int, input().split()))
min_val = arr[0]
# for val in arr:
#     if val < min_val:
#         min_val = val

for val in arr:
    min_val = val if val < min_val else min_val

print(min_val)



