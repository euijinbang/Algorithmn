class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_nums = []
        for i in range(len(number)):
            if number[i] == digit:
                max_nums.append(int(number[:i]+ number[i+1:]))
        max_nums.sort()
        return str(max_nums[-1])

# 매번 max 구하는것보다 배열에 넣고 sort하는게 더 빠르다.

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for i in range(len(number)):
            if number[i] == digit:
                max_num = max(max_num, int(number[:i]+ number[i+1:]))
        return str(max_num)

# 인덱스 접근이 enumerate 보다 빠르다.

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_num = 0
        for i, val in enumerate(number):
            if val == digit:
                max_num = max(max_num, int(number[:i] + number[i+1:]))

        return str(max_num)