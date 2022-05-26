class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def backtrack(subset, start):
            ans.append(subset.copy())  # 매번 추가

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i+1)
                subset.pop()

        backtrack([], 0)
        return ans