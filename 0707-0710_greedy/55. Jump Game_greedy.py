class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        << greedy >>
        last index를  goal로 잡고
        index를 맨 뒤부터 0까지 가져오는데
        index + nums[index] >= goal 이라면 곧
        goal에 도착할 수 있다는 의미이므로
        goal 을 index에 이동시키고 그다음 index를 확인
        goal 이 0 에 도착하면 True 반환
        """

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            # 해당 인덱스에서 goal까지 이동가능하다는 의미
            if i + nums[i] >= goal:
                goal = i  # goal 이동

        return True if goal == 0 else False
