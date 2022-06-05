class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2))[2:]

        # sol2.
        # total = 0
        # m, n = len(a), len(b)
        #
        # for i in range(m):
        #     total += (2 ** (m-i-1)) * int(a[i])
        #
        # for j in range(n):
        #     total += (2 ** (n-j-1)) * int(b[j])
        #
        # return format(total, 'b')

# int(value, base)
# value:  A number or a string that can be converted into an integer number
# base:   A number representing the number format. Default value: 10


