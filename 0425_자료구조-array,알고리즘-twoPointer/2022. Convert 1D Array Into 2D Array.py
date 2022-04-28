class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []

        result = []

        for i in range(m):
            result.append(original[n * i : n * (i+1)])


        return result