"""
배열에서 중복된 숫자가 나오면 True를 반환
"""

# 인덱스 비교 => 시간초과
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

# sort 오름차순 정렬 해놓고 연속된 인덱스만 비교
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


# SET(해시테이블) 사용 (BEST!!!)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True

            s.add(num)

        return False

# 딕셔너리(해시테이블) 사용
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            try:
                counter[num] += 1
                if counter[num] == 2:
                    return True
            except:
                counter[num] = 1

        return False