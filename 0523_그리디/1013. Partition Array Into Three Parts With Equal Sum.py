class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3: return False

        # 쭉 더하며 확인, cnt 3이상 반환 ... 0일경우 3이상
        cnt, tmp, target = 0, 0, total // 3
        for n in arr:
            tmp += n
            if tmp == target:
                cnt += 1
                tmp = 0
        return cnt >= 3

####################################################################

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0: return False
        count, cumsum, target = 0, 0, total // 3
        for num in A:
            cumsum += num
            if cumsum == target:
                cumsum = 0
                count += 1
        return count >= 3