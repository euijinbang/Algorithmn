class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for char in "{:032b}".format(n):    # 정수를 32bit 문자열로 변경
            if char == "1": cnt += 1

        return cnt

        # or...
        return bin(n).count("1")