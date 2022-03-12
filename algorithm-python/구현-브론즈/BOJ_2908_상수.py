list1, list2 = map(list, input().split())

new_list1 = []
for i in range(len(list1)-1, -1, -1): # 2, 1, 0 index
    new_list1.append(list1[i])

new_list2 = []
for i in range(len(list2)-1, -1, -1): # 2, 1, 0 index
    new_list2.append(list2[i])

n_list = [int(''.join(new_list1)), int(''.join(new_list2))]
print(max(n_list))
