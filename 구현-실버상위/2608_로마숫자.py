nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
extra = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}


def to_nums(S):
    check = [0] * len(S)
    total = 0
    for i in range(len(S)):
        if not check[i]:
            if i+1 < len(S) and S[i:i+2] in extra:
                tmp = S[i:i+2]
                total += extra[tmp]
                check[i:i+1] = 1, 1
            else:
                total += nums[S[i]]
                check[i] = 1
    return total


"""
..ing..
"""

A = 'DLIII'
B = 'MCMXL'

print(to_nums(A))
print(to_nums(B))
