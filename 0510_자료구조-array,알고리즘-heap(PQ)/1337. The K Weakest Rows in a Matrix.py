# 내풀이 - 튜플 및 sort 활용
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])
        d = [0] * m
        for i in range(m):
            s = 0
            for j in range(n):
                if mat[i][j] == 1:
                    s += 1
            d[i] = (s, i)

        sorted_d = sorted(d, key=lambda x:x[0])
        result = []
        turn = 1
        for info in sorted_d:
            if turn == k:
                result.append(info[1])
                return result
            result.append(info[1])
            turn += 1


# 군인 수를 바이너리 서치로 찾는경우
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Binary Search
        def getSoldierNum(info):
            l, r = 0, len(info)
            while l < r:
                mid = (l+r) // 2
                if info[mid] > 0:
                    l = mid + 1
                else:
                    r = mid
            return l

        info = []
        for i, row in enumerate(mat):
            info.append((getSoldierNum(mat[i]), i))

        info.sort()
        return [info[i][1] for i in range(k)]


#############################################################################

### 1. (count, index) 튜플 형태로 만든다.
### 2. k smallest 면 [:k] 로 배열을 자르거나, heapq 모듈인  nsamllest를 이용한다.
# sol1. 0이 처음 등장하는 인덱스 == 1의 갯수 => binarySearch 로 찾는다.
from heapq import nsmallest

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for count, i in nsmallest(k, ((self.count_ones(row), i) for i, row in enumerate(mat)))]

    def count_ones(self, a):
        x, lo, hi = 0, 0, len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if a[mid] > x: lo = mid+1
            else: hi = mid
        return lo

# sol2. 축약형 코드
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        matIndexAndSumRow = [[sum(val),idx] for idx,val in enumerate(mat)]
        matIndexAndSumRow.sort()
        return [matIndexAndSumRow[i][-1] for i in range(k)]