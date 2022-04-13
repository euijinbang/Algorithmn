nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    """
    차이(target - 현재 값)이 해시테이블에 있다면 차이와 현재값의 인덱스를 반환
    """
    hashMap = {}  # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return [hashMap[diff], i]

        # 차이값이 해시테이블에 없다면 저장
        hashMap[n] = i


print(twoSum(nums, target))
