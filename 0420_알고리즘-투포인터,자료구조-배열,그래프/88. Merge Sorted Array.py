"""
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3


nums1 의 0이 아닌 부분의 맨 뒤 인덱스, nums2 맨 뒤 인덱스부터 비교하면서
큰 수를 nums1 끝부터 채워나간다.
채울때마다 해당 인덱스 포인터를 1 감소시킨다.
"""
nums1 = [2,2,3,0,0,0]
m = 3
nums2 = [1,5,6]
n = 3

# last index nums1
last = m + n - 1

# merge in reverse order
while m > 0 and n > 0:
    if nums1[m - 1] > nums2[n - 1]:
        nums1[last] = nums1[m - 1]
        m -= 1
    else:
        nums1[last] = nums2[n - 1]
        n -= 1
    last -= 1

# fill nums1 with leftover nums2 elements
# nums1이 남으면 그대로 가면 되는데, nums2가 남으면 nums1에 넣어주어야 한다.
while n > 0:
    nums1[last] = nums2[n - 1]
    n, last = n - 1, last - 1










# 하나하나 비교하는 풀이(아마 통과 못할듯)
# result = []
# l1, l2 = 0, 0
#
# while l1 < m:
#     if nums1 and not nums2:
#         print(nums1)
#         break
#
#     if nums1[l1] == nums2[l2]:
#         result.append(nums1[l1])
#         result.append(nums2[l2])
#         l1 += 1
#         l2 += 1
#
#     if nums1[l1] < nums2[l2]:
#         result.append(nums1[l1])
#         l1 += 1
#     else:
#         result.append(nums2[l2])
#         l2 += 1
#
# for i in range(l2, n):
#     result.append(nums2[i])
#
# print(result)