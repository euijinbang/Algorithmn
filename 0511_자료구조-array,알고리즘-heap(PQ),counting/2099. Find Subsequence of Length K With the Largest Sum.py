class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        max_k = sorted(nums, reverse=True)[:k]
        result = []
        for num in nums:
            if num in max_k:
                result.append(num)
                max_k.remove(num)
                if not max_k:
                    return result




#######################################
class Solution(object):
    def maxSubsequence(self, nums, k):
        ret, max_k = [], sorted(nums, reverse=True)[:k]
        for num in nums:
            if num in max_k:
                ret.append(num)
                max_k.remove(num)
                if len(max_k) == 0:
                    return ret