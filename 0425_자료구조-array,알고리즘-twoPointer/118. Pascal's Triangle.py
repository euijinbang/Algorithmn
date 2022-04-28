class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 1. 모두 1로 채운다.
        n = numRows

        pascal = []
        for i in range(n):
            pascal.append([1] * (i + 1))


        # 2. 위부터 내려오면서 r, c에서 r = n - 1 인덱스이고 c는 1부터 r-1까지 반복,
        #    (m, n)을 위 행의 두 숫자의 합(m-1, n-1) + (m-1, n)으로 갱신한다.

        for r in range(2, n):
            for c in range(1, r):
                pascal[r][c] = pascal[r-1][c-1] + pascal[r-1][c]

        return pascal