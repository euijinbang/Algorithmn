class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # nums1이 항상 짧도록 한다.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # nums1을 돌면서 해쉬맵을 만든다.
        hashMap = {}
        for num in nums1:
            hashMap[num] = hashMap.get(num, 0) + 1 # 없다면 0을 디폴트로 가져온다.

        # nums2를 돌면서 이를 해쉬맵에서 찾고, 찾으면 답에 더하고 해쉬맵 value를 1 감소한다.
        answer = []
        for num in nums2:
            count = hashMap.get(num, 0) # keyerror 방지
            if count > 0:
                answer.append(num)
                hashMap[num] -= 1


        return answer