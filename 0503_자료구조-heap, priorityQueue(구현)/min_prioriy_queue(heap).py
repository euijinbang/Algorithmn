"""
heapq 모듈은 최소 우선순위 큐를 지원한다.
key와 data를 push 하면 key가 작은 원소가 앞에 위치한다.
key가 높은 원소부터 꺼내고 싶으면 뒤집자.
루트 인덱스는 0이다.
"""
from heapq import heappush, heappop

h = []
heappush(h, (4, 'kim'))
heappush(h, (3, 'lee'))
heappush(h, (1, 'jong'))
heappush(h, (2, 'seo'))

heappop(h)

print(h[0])
print(h[-1])

res = []
while h:
    res.append(heappop(h))
print(res[::-1])

##############################



class Element:
    def __init__(self, key, string):
        self.key = key
        self.data = string


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        if not self.heap:
            return True
        return False

    def push(self, item):
        heappush(self.heap, (item.key, item.data))  # key를 기준으로 정렬한다.

    def pop(self):
        return heappop(self.heap)

    def min(self):
        return self.heap[0]


if __name__ == "__main__":
    pq = MinPriorityQueue()

    pq.push(Element(2, "kim"))
    pq.push(Element(1, "park"))
    pq.push(Element(3, "lee"))
    pq.push(Element(5, "seo"))

    while not pq.is_empty():
        elem = pq.pop()
        print(f"key[{elem[0]}] : data[{elem[1]}]")