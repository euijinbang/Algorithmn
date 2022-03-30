N = input()


def lucky(N):
    left, right = 0, 0
    nums = list(map(int, N))

    for i in range(len(nums)//2):
        left += nums[i]
        right += nums[len(nums) - i - 1]

    if left == right:
        answer = "LUCKY"
    else:
        answer = "READY"

    return answer


print(lucky(N))
