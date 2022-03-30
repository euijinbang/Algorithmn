list = [1, 2, 3, 4]

# append
list.append(5)
print(list)
# [1, 2, 3, 4, 5]


# del: 해당 인덱스의 요소 삭제
del list[0]
print(list)
# [2, 3, 4, 5]


# insert: 인덱스 4번 위치에 6 삽입
list.insert(4, 6)
print(list)
# [2, 3, 4, 5, 6]

##########################################
numbers = [9, 4, 2, 6, 5]

# sorted : 원본리스트 유지하고 정렬된 새로운 리스트 리턴
new_list = sorted(numbers)
print(f"new_list: {new_list}")
# new_list: [2, 4, 5, 6, 9]

print(f"numbers: {numbers}")
# numbers: [9, 4, 2, 6, 5]

new_list = sorted(numbers, reverse=True)
print(f"new_list: {new_list}")
# new_list: [9, 6, 5, 4, 2]


# sort() : 리턴값 없이 원본리스트를 정렬
numbers.sort()
print(numbers)
# [2, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)
# [9, 6, 5, 4, 2]

# reverse() : 리턴값 없이 원본리스트를 정렬
numbers.reverse()
print(numbers)
# [2, 4, 5, 6, 9]

# index(x) : x의 값을 가지고 있는 원소의 인덱스를 리턴
print(numbers.index(2))
# 0

# remove(x) : x의 값을 가진 원소를 처음부터 삭제
numbers.remove(4)
print(numbers)
# [2, 5, 6, 9]