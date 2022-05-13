"""
bin library 사용, sort 기준 2개
"""

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        unsorted = []
        for num in arr:
            unsorted.append((num , sum([int(x) for x in format(num, 'b')])))
        # 1의 갯수가 같으면 오름차순으로 정렬
        sorted_num = sorted(unsorted, key=lambda x: (x[1], x[0]))
        result = [x[0] for x in sorted_num]
        return result


#######################
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))