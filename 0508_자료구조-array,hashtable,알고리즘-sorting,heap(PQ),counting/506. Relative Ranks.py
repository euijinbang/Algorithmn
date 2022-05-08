

# 배열사용
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)
        #[점수, 들어온 순서]를 저장
        scores = []
        for idx, s in enumerate(score):
            scores.append([s, idx])
        #점수를 기준으로 높은 점수 순으로 정렬
        ranked_scores = sorted(scores, key=lambda x : x[0], reverse=True)
        #[[10, 0], [9, 3], [8, 2], [4, 4], [3, 1]]
        print(ranked_scores)
        #해당 점수순으로 메달을 부여 - result 배열 만들어두고
        #인덱스를 활용
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[ranked_scores[i][1]]= "Gold Medal"
            elif i == 1:
                result[ranked_scores[i][1]] = "Silver Medal"
            elif i == 2:
                result[ranked_scores[i][1]] = "Bronze Medal"
            else:
                result[ranked_scores[i][1]] = str(i+1)

        return result


# 딕셔너리 사용
def findRelativeRanks(self, nums: List[int]) -> List[str]:

    # Sort scores from best to worst
    nums_sorted = sorted(nums, reverse = True)

    # Map each sorted score to its index
    s = {score : index for index, score in enumerate(nums_sorted)}

    # Create list of medals in ascending order
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(nums) + 1)]

    # Generate the list of medals in order
    result = [medals[s[n]] for n in nums]
    return result