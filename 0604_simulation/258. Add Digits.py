class Solution:
    def addDigits(self, num: int) -> int:
        """
        38 -> ['3', '8'] -> total 11
           -> ['1', '1'] -> total 2
        """

        while num // 10:
            total = 0
            num = list(str(num))
            while len(num) > 0:
                total += ord(num.pop()) - ord('0')

            num = total

        return num