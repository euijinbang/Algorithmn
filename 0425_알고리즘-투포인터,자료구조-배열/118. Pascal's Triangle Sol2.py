class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # [[1]] 로 base case를 초기화한다.
        # 리스트[-1] 을 꺼내서 양옆에 0을 붙여 j인덱스를 옮겨가며 계산한다.

        res = [[1]]
        for i in range(numRows - 1):
            temp = [0] + res[-1] + [0]

            nextRow = []
            for j in range(len(res[-1]) + 1):
                nextRow.append(temp[j] + temp[j+1])

            res.append(nextRow)

        return res