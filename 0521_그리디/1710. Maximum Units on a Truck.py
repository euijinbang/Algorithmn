
# sol2 활용=> 실행속도가 10배 이상 빠르다..
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        answer = 0
        for numBox, numUnitsPerbox in boxTypes:
            n = min(numBox, truckSize)
            answer += n * numUnitsPerbox
            truckSize -= n   # truckSize 에서 쌓은 상자 갯수를 뺀다.
            if truckSize == 0:
                break
        return answer

# sol1(처음 내풀이) 변수로 체크
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        answer, boxNum = 0, 0
        for box in boxTypes:
            boxNumTmp = 0
            while boxNumTmp < box[0] and boxNum < truckSize:
                boxNum += 1
                boxNumTmp += 1
                answer += box[1]
        return answer

# sol2. capacity에서 빼는 풀이
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=1)
        s=0
        for i,j in boxTypes:
            i=min(i,truckSize)
            s+=i*j
            truckSize-=i
            if truckSize==0:
                break
        return s