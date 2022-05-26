from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # sol1. itertools
        # return list(itertools.permutations(nums))

        # sol2. visited check
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

        # sol3. prev and next
        ans = []
        prev_nums = []

        def backtrack(nums):
            if len(nums) == 0:
                ans.append(prev_nums.copy())

            for n in nums:
                next_nums = nums.copy()
                next_nums.remove(n)

                prev_nums.append(n)
                backtrack(next_nums)
                prev_nums.pop()

        backtrack(nums)
        return ans
