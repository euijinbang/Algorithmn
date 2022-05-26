# sol1. 양옆 조건 걸어주기
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, p in enumerate(flowerbed):
            # 해당 자리, 좌, 우가 모두 0이면 1로 바꾼다.
            if (not p
                    and (i == 0 or flowerbed[i-1] == 0)
                    and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n -= 1

        return n <= 0

# sol2. 패딩과 더하기
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n


# sol3. single scan
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                # 처음이면 좌측이 True, 끝이면 우측이 True
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                # If both plots are empty, we can plant a flower here.
                # 둘다 True여야 True
                if empty_left and empty_right:

                    flowerbed[i] = 1
                    count += 1

        return count >= n



# 초기 내풀이 => 중복도 많고.. 처음과 끝일때 처리 다시 생각해보자!
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and i+1 < len(flowerbed):
                    if flowerbed[i+1] == 1: continue
                if i == len(flowerbed)-1 and i-1 >= 0:
                    if flowerbed[i-1] == 1: continue
                if i != 0 and i != len(flowerbed)-1:
                    if flowerbed[i-1] == 1 or flowerbed[i+1] == 1 : continue
                flowerbed[i] = 1
                n -= 1
                if n == 0: return True
        return False if n else True
