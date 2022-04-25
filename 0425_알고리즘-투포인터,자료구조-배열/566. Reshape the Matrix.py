class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat

        # 1. 이차원 배열 -> 일차원 배열

        array_1d = [10001] * m * n

        for i in range(m):
            for j in range(n):
                array_1d[n * i + j] = mat[i][j]

        # 2. 일차원 배열 -> 이차원 배열 (열 만큼 건너뛰는것에 주의!)

        array_2d = []

        for row in range(r):
            array_2d.append(array_1d[c * row : c * (row+1)])

        return array_2d