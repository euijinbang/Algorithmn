class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r, n = 0, len(numbers) - 1, len(numbers)

        # 좌측 포인터는 0부터, 우측 포인터는 맨 오른쪽에서 시작
        # 좌우측 포인터가 가리키는 값의 합이 target보다 크면 우측 포인터를 내리고, 작으면 좌측 포인터를 올린다.
        # 더한 값이 타겟이면 인덱스를 리턴한다.
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

