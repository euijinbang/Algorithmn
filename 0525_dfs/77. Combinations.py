class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 시작 index 조정으로 중복방지
        ans = []
        def backtrack(depth, comb, start):
            if depth == k:
                ans.append(comb.copy())
                return

            for i in range(start, n+1):
                comb.append(i)
                backtrack(depth+1, comb, i+1)
                comb.pop()

        backtrack(0, [], 1)
        return ans
