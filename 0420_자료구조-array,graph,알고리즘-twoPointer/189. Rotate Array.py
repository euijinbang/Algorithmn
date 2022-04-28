# 인덱스 투포인터 사용
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums 자체로 바꿔야하므로 654321 로 만든 후에, 456 123 이렇게 잘라서 다시 swap한다.
        # 1. l, r 인덱스 정하고
        # 2. l < r일때 좌우 바꾼다.
        # 3. l 부터 k-1 인덱스까지 swap, k부터 r 인덱스까지 swap한다.

        k = k % len(nums)  #[-1], 2가 들어오면 이거 없으면 index out of range 발생함. 나머지만큼만 회전하면된다.

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1


# 인덱스 더해가는 풀이
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        result = [0] * n

        for i in range(n):
            if i + k >= n:
                result[(i+k) % n] = nums[i]  # i+k 가 전체 길이를 넘어가면 n으로 나눈 나머지를 구한다.
            else:
                result[i+k] = nums[i]

        nums = result


