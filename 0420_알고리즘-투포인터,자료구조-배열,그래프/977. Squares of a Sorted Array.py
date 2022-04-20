"""
인덱스를 바깥에서부터 좌우 비교하며 진행
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        l, r = 0, len(nums) - 1

        while l <= r:   # 같아질 때 가운데 수까지 넣고 종료
            if nums[l] * nums[l] < nums[r] * nums[r]:
                result.append(nums[r] * nums[r])
                r -= 1
            else:
                result.append(nums[l] * nums[l])
                l += 1

        return result[::-1]  # 결과 역순으로 출력(큰수부터 더했으므로)