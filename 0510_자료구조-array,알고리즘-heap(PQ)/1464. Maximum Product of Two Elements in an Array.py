class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # sol1
        # sorted_nums = sorted(nums, reverse=True)
        # return (sorted_nums[0]-1) * (sorted_nums[1]-1)

        # sol2  - 일일이 비교하는 방법, 좀 더 정석적인 풀이가 아닌가..
        first, second = 0, 0
        for num in nums:
            if num > first:
                first, second = num, first
            elif num > second:
                second = num

        return (first-1) * (second-1)