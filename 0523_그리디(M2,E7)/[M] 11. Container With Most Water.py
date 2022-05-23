class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Linear time solution(O(n))
        two-pointer 사용
        더 작은 높이쪽의 포인터를 움직인다.
        매번 움직일때 마다 최댓값을 갱신한다.
        """
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return res