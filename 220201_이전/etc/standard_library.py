# import math
#
# print(math.log10(100))
# print(math.cos(0))
# print(math.pi)


import random

# random 함수: 0과 1 사이의 랜덤한 소수를 리턴
print(random.random())
# 0.5037250290115692


# randint 함수: 두 수 사이의 랜덤한 정수를 리턴(이상 이하)
print(random.randint(1, 20))
# 13


# randrange 함수: 두 수 사이의 랜덤한 정수를 리턴(이상 "미만")
# random.randrange(start, stop, step)
print(random.randrange(3, 6))
# 4


# uniform 함수: 두 수 사이의 랜덤한 소수를 리턴(이상 이하)
print(random.uniform(0, 1))
# 0.06446766764370038


# choice: 하나의 원소를 랜덤으로 뽑아 리턴
nums = [1, 2, 3]
print(random.choice(nums))
# 3


# import os
#
# print(os.getlogin())
# print(os.getcwd())