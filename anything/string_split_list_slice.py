"""
문자열은 slicing으로 자른다.
"""
a = "abcde"
sliced_a = a[0:len(a)]
print(sliced_a)
# abc

"""
문자열은 split 으로 나눈다.
"""
b = "ab c de"
splited_b = b.split()
print(splited_b)
# ['ab', 'c', 'de']

"""
리스트는 slice 로 자른다.
"""
c = [1, 2, 3, 4, 5]
sliced_c = c[0:3]
print(sliced_c)
# [1, 2, 3]
