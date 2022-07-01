class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)
        answer = 0
        for numBox, numUnitsPerbox in boxTypes:
            n = min(numBox, truckSize)
            answer += n * numUnitsPerbox
            truckSize -= n
            if truckSize == 0:
                break
        return answer
