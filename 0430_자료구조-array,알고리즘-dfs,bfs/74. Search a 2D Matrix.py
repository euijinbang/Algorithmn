class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(data, target):
            l, r = 0, len(data) - 1
            while l <= r:
                mid = (l + r) // 2
                if target == data[mid]:
                    return True
                if target < data[mid]:
                    r = mid - 1
                if target > data[mid]:
                    l = mid + 1
            return False

        for row in matrix:
            if target <= row[-1]:
                if binarySearch(row, target):
                    return True
        return False
