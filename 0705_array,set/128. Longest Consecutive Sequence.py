class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        # Brute Force
        숫자 돌면서 n + 1 이 있는지 모든 배열을 돌면서 확인
        => time limit exceed

        # numSet
        # set으로 만든 후, n - 1 이 numSet에 없다면 카운트를 시작
        # 1씩 증가시키면서 numSet에 있는지 확인한다.
        """
        # numSet
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

        # Brute Force
#         longest_streak = 0

#         for n in nums:
#             cur_n = n
#             cur_streak = 1

#             while cur_n + 1 in nums:
#                 cur_n += 1
#                 cur_streak += 1

#             longest_streak = max(longest_streak, cur_streak)

#         return longest_streak