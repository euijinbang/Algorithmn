class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def backtracking(depth, comb):
            if depth == k:
                ans.append(comb.copy())
                return

            for i in range(1, n+1):
                #visited 필요없고, 이전 수보다 큰 수만 넣는다.
                if i > comb[-1] if comb else True:
                    comb.append(i)
                    backtracking(depth+1, comb)
                    comb.pop()

        backtracking(0, [])
        return ans
