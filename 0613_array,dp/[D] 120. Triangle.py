class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        DP: start from the last row

        min(3[0]+2[0], 3[1]+2[0]) => 2[0]
        min(3[1]+2[1], 3[2]+2[1]) => 2[1]
        min(3[2]+2[2], 3[3]+2[2]) => 2[2]

        min(2[0]+1[0], 2[1]+1[0]) => 1[0]
        min(2[1]+1[1], 2[2]+1[1]) => 1[1]

        min(1[0]+0[0], 1[1]+0[0]) => 0[0]

        """

        for i in range(len(triangle)-1, 0, -1):
            for j in range(i):
                left = triangle[i][j] + triangle[i-1][j]
                right = triangle[i][j+1] + triangle[i-1][j]
                triangle[i-1][j] = min(left, right)

        return triangle[0][0]
