#sol1
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            x = stones.pop()
            if not stones:
                return x
            y = stones.pop()
            if x > y:
                #insert할 위치를 찾기
                for i in range(len(stones)+1):
                    print(stones)
                    # 맨 마지막에 들어가는 경우도 포함
                    if i == len(stones) or stones[i] > x-y:
                        stones.insert(i, x-y)
                        break
        return 0

#sol2
from heapq import heapify, heappush, heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapify(h)
        print(h)
        while h:
            s1 = -heappop(h)
            if not h:
                return s1
            s2 = -heappop(h)
            if s1 > s2:
                print(s1-s2)
                heappush(h, -(s1-s2))

        return 0


###############################################################
# sort-pop 접근법
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # the remaining stone will be s1-s2
                # loop through stones to find the index to insert the stone
                for i in range(len(stones)+1):
                    if i == len(stones) or stones[i] >= s1-s2:
                        stones.insert(i, s1-s2)
                        break
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain

# heapq 자료구조 사용
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # first, negate all weight values in-place
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)  # pass all negated values into the min-heap
        while stones:
            s1 = -heappop(stones)  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                heappush(stones, s2-s1)  # push the NEGATED value of s1-s2; i.e., s2-s1
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain

#################################################
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        while True:
            second, first = stones.pop(), stones.pop()
            if first <= second:
                if first < second:
                    stones.append(second - first)
                    stones.sort()
            if len(stones) == 1:
                return stones[0]
            if len(stones) == 0:
                return 0

###### heapq 사용 ######
    ### -를 붙여서 작은수부터 정렬
    def lastStoneWeight(self, A):
        h = [-x for x in A]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h, heapq.heappop(h) - heapq.heappop(h))
        return -h[0]

###### sort 사용 #######
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            second, first = stones.pop(), stones.pop()
            stones.append(second - first)
            stones.sort()
        return stones[-1]