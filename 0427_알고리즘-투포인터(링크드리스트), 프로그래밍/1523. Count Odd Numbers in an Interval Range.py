class Solution:
    def countOdds(self, low: int, high: int) -> int:

        # high - low + 1 이 짝수이면 홀수와 짝수의 갯수가 같다.
        # high - low + 1 이 홀수인데 low가 홀수이면 홀수갯수 = 전체갯수//2 + 1
        # high - low + 1 이 홀수인데 low 가 짝수이면 홀수갯수 = 전체갯수//2

        total = high - low + 1
        if total % 2:
            if low % 2:
                return total // 2 + 1
            else:
                return total // 2
        else:
            return total // 2
