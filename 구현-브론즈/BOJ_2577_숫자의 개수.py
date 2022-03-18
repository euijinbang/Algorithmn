"""
딕셔너리 활용
정수와 문자열 변환
"""
nums = []
for i in range(3):
    nums.append(int(input()))
# nums = [1, 2, 100]

total = 1
for n in nums:
    total *= n

total_char = str(total)
total_char_list = [x for x in total_char]

num_dict = {}
for i in range(10):
    num_dict[i] = 0

for one_char in total_char_list:
    num_dict[int(one_char)] += 1

for val in num_dict.values():
    print(val)
