class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        visited = set()
        ans = []
        def backtracking(depth, res):
            if depth == len(nums):
                ans.append(res.copy())
                return

            for n in nums:
                if n not in visited:
                    res.append(n)
                    visited.add(n)
                    backtracking(depth+1, res)
                    res.pop()
                    visited.remove(n)

        backtracking(0, [])
        return ans
