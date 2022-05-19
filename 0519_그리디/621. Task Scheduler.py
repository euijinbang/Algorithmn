from heapq import heappush, heappop, heapify
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-x for x in counter.values()]
        heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heappop(max_heap)
                if cnt:
                    q.append((cnt, time + n)) #time+n번째 부터 들어갈 수 있다
            if q and q[0][1] == time:
                heappush(max_heap, q.popleft()[0])
        return time