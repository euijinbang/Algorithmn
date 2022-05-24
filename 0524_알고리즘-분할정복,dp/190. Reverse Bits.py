### pythonic
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = '{:032b}'.format(n)  # '{:032b}'.format(n) => n을 32비트 2진수로 변환
        integer = int(binary[::-1], 2)  # 2진수를 10진수 정수로 변환
        return integer