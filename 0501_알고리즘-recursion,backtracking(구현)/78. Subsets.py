class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #별도의 return 없이도 탐색이 끝나면 함수가 종료된다
        res = []
        def backtrack(index, sub):
            res.append(sub)

            for i in range(index, len(nums)):
                backtrack(i+1, sub + [nums[i]])

        backtrack(0, [])

        return res