class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        1 1 4 2 3  x = 5 라면 sum(nums) - x 의 값인 "6" 을 합으로 하는 최장 subarray size 구한다.
        "6" 을 합으로 하는 subarray를 찾으면 길이를 갱신한다.
        "6" 을 초과하면 "6" 이하가 될 때 까지 좌측인덱스를 슬라이딩한다.
        다 돌면 전체 길이에서 max subarray size 를 뺀다.

        """
        arr_sum = sum(nums)
        if arr_sum < x:
            return -1
        if arr_sum == x:
            return len(nums)

        required_subarray_sum = arr_sum - x
        left = curr_sum = max_subarray_size = 0
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum > required_subarray_sum:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == required_subarray_sum:
                max_subarray_size = max(max_subarray_size, right - left + 1)

        return len(nums) - max_subarray_size if max_subarray_size > 0 else -1