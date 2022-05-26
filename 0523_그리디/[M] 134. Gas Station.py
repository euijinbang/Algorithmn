class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        1. sum(gas) >= sum(cost) 라면 route를 보장한다.
        2. gas[i] - cost[i] < 0 이라면 그 지점에서 시작할 수 없다.
        3. 돌다가 total 이 한번이라도 음수라면 그 지점에서 시작할 수 없다.

        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        diff = [-2,-2,-2,3,3]

        """
        if sum(gas) < sum(cost) : return -1

        total = 0
        start = 0     # starting position

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                start = i + 1

        return start