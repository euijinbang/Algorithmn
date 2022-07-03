class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # 각각의 Cuts를 오름차순 정렬
        # Cuts 맨 앞과 맨 뒤에 0과 h, w를 각각 넣는다.
        # 각 Cuts의 연속된 element의 차이의 최댓값을 구한다.

        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        max_hc = 0
        for i in range(1, len(horizontalCuts)):
            max_hc = max(max_hc, horizontalCuts[i] - horizontalCuts[i-1])

        max_vc = 0
        for i in range(1, len(verticalCuts)):
            max_vc = max(max_vc, verticalCuts[i] -verticalCuts[i-1])

        return (max_hc * max_vc) % (10**9 + 7)
