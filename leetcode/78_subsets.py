"""
주어진 리스트에는 중복값이 없다.
중복 없이 모든 subset을 구한다.
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""


def subsets(nums):
    """
    i : index
    """
    result = []
    subset = []

    def dfs(i):
        # 종료조건
        if i >= len(nums):
            result.append(subset.copy())
            return

        # 선택 경우의 수가 2개이므로 for문 쓸 필요 없다.
        # nums[i] 를 포함하는 선택
        subset.append(nums[i])
        dfs(i + 1)

        # nums[i] 를 포함하지 않는 선택
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return result


print(subsets([1, 2, 3]))
