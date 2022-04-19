# 0 또는 양의 정수가 주어졌을 때, 정수를 이어붙여 만들 수 있는 가장 큰 수

numbers = [6, 10, 2]
n = len(numbers)


class compare(str):
    def __lt__(a, b):
        if a + b > b + a:
            return True
        else:
            return False

def solution(numbers):
    numbers = list(map(str, numbers))

    answer = sorted(numbers, key=compare)
    return str(int("".join(answer)))


# print(solution([6, 10, 2]))

nums = [(1, 4), (2, 5), (3, 1)]
nums.sort(key=lambda x: x[1])
print(nums)

s_nums = sorted(nums, key=lambda x: x[0])
print(s_nums)
