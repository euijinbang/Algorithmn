"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
"""


def combinations(n, k):
    res = []

    def backtrack(start, comb):
        if len(comb) == k:
            res.append(comb.copy())
            return

        for i in range(start, n + 1):
            comb.append(i)
            backtrack(i + 1, comb)
            comb.pop()

    backtrack(1, [])
    return res


print(combinations(4, 2))
