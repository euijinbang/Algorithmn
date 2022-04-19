class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        """
        hashmap  {num : count}
        """
        # count 를 갱신하는 보이어-무어 알고리즘
        # res, count = 0, 0
        #
        # for n in nums:
        #     if count == 0:    # 초기세팅 & count 0 일때 최빈값 업데이트
        #         res = n
        #
        #     count += (1 if res == n else -1) # count 를 늘렸다가, 다른 수가 나오면 줄인다


        count = {}
        res, maxCount = 0, 0

        for n in nums:
            # 각 수가 나온 횟수를 구해서 딕셔너리에 저장
            count[n] = 1 + count.get(n, 0)
            # 나온 횟수가 더 크면 답을 갱신
            res = n if count[n] > maxCount else res
            # 최대 카운트를 갱신
            maxCount = max(count[n], maxCount)


        return res
