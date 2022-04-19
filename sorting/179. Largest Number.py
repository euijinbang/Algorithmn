nums = [10, 2, 540]

# 1. 문자열 리스트로 변환한다.
for i, n in enumerate(nums):
    nums[i] = str(n)
# 또는
nums = list(map(str, nums))

# 2. 정렬 기준 함수를 만든다. # 리턴값 기준 정렬
class largerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
        # x > y 이면 true 이므로 유지, x < y 이면 false 이므로 순서 변환

# 3. 정렬 기준대로 정렬한다.
nums = sorted(nums, key=largerNumKey)
ans = "".join(nums)
print(ans)
