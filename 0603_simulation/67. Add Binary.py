class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = 0
        m, n = len(a), len(b)

        for i in range(m):
            total += (2 ** (m-i-1)) * int(a[i])

        for j in range(n):
            total += (2 ** (n-j-1)) * int(b[j])

        return format(total, 'b')
