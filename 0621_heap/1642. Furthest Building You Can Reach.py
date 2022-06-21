from heapq import heappush, heappop

class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, ladders: int) -> int:

        """
        heap : ladder를 사용해야하는 간격을 저장
        빌딩
        0 1 2 3 4 5  6
        4 2 7 6 9 14 12
        minHeap
        []
        [5]
        [3, 5] => [5] 쓴 벽돌 3 남은 벽돌 2
        [5, 5] => [5] 쓴 벽돌 5 남은 벽돌 -3
        벽돌이 다 떨어졌으므로 i인 4를 리턴

        빌딩
        1  2  3 4
        14 3 19 3 /17/0
        []
        [16] => [] 쓴 벽돌 16 남은 벽돌 1
        끝까지 도착

        """

        minHeap = []
        for i in range(len(h)-1):
            d = h[i+1] - h[i]
            if d > 0:
                heappush(minHeap, d)

            # pq의 사이즈가 사다리개수보다 많다 => brick 사용
            if len(minHeap) > ladders:
                # 가장 작은 간격부터 벽돌을 사용한다.
                bricks -= heappop(minHeap)
            # 벽돌이 다 떨어지면 순서를 리턴한다.
            if bricks < 0:
                return i

                # 끝까지 도착하면 길이-1 을 리턴
        return len(h)-1


