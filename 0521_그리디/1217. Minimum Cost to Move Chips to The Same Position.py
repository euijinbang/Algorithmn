class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # +2, -2 는 0이므로 모든 홀수위치 동전은 1로, 짝수위치 동전은 0으로 이동
        # 이후 더 적은 쪽을 움직인다.

        pos = [0, 0]
        for p in position:
            if p % 2: pos[1] += 1
            else: pos[0] += 1

        return min(pos[0], pos[1])