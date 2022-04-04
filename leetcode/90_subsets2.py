"""
주어진 리스트에는 중복값이 있다.
중복 없이 모든 subset을 구한다.
sort 된 값을 구한다.
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [4,4,4,1,4]
Output: [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

가지치기
"""


def subsetsWithDup(nums):
    """
    i : index
    """
    nums.sort()
    result = []
    subset = []

    def backtrack(i):
        # 종료조건
        if i >= len(nums):
            result.append(sorted(subset[:]))  # copy() 필수
            return

        # 선택 경우의 수가 2개이므로 for문 쓸 필요 없다.
        # nums[i] 를 포함하는 선택
        subset.append(nums[i])
        backtrack(i + 1)

        # nums[i] 를 포함하지 않는 선택
        subset.pop()
        # nums의 현재 인덱스값과 다음 인덱스값을 비교해서, 다른 값이 나오면 그때 다음 깊이로 넘어간다.
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1)

    backtrack(0)
    return result


# print(subsetsWithDup([4, 4, 4, 1, 4]))
print(subsetsWithDup([1, 2, 2]))
