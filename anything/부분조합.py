"""
N = 3
1, 4, 7로 만들 수 있는 모든 경우의 수
== 부분조합
첫 뎁스에 1을 선택할지말지 2개로
다음 뎁스에 4를 선택할지말지 2개로
다음 뎁스에 7을 선택할지말지 2개로
"""
N = 3
nums = [1, 4, 7]

result = []
def get_subset(i, subset):
    if i == N:  # 인덱스 초과하면 리턴
        result.append(subset[:])
        return

    # 선택 하는 경우, 안하는 경우니까 for문 쓰지 않는다.
    # nums[i] 를 포함하는 선택
    subset.append(nums[i])
    get_subset(i + 1, subset)

    # nums[i] 를 포함하지 않는 선택
    subset.pop()
    get_subset(i + 1, subset)

    return result


print(get_subset(0, []))

