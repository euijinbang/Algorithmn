"""
sort, index를 잘 활용, min 업데이트
"""
def minimunDifference(self, nums: List[int], k:int) -> int:
    nums.sort()
    answer = sys.maxsize
    for i in range(0, len(nums)-k+1):
        val = nums[i+k-1] - nums[i]  # 1 - 0 / 2 - 1
        answer = min(answer, val)

    return answer

################# 내풀이
nums.sort()
answer = sys.maxsize
for i in range(len(nums)-k+1):
    tmp = []
    for j in range(i, i+k):
        tmp.append(nums[j])
    answer = min(answer, (tmp[-1]-tmp[0]))
return answer