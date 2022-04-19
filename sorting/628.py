perms = []


def permutation(start, comb):
    global maxProduct
    """
    인덱스를 뎁스처럼 생각하면 된다
    3개를 뽑는다
    """
    if len(comb) == 3:
        tempProduct = 1
        perms.append(comb.copy())
        # 조치...(최대값 갱신)
        for c in comb:
            tempProduct *= c
        maxProduct = tempProduct if tempProduct > maxProduct else maxProduct
        return

    for i in range(start, len(nums)):
        comb.append(nums[i])
        permutation(i + 1, comb)
        comb.pop()

maxProduct = 1
nums = [1, 2, 3, 4]
permutation(0, [])
print(maxProduct)
