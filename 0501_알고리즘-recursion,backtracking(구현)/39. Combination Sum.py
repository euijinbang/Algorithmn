class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        #range 범위조정이 핵심 - 다음 인덱스 범위부터 돌려서 중복을 방지  [2,2,3] [3,2,2]

        res = []
        candidates.sort()
        def backtrack(target, index, sub):
            if target < 0:
                return
            if target == 0:
                res.append(sub)
                return

            # 인덱스 범위 조정하여 중복방지!!!
            for i in range(index, len(candidates)):
                backtrack(target-candidates[i], i, sub+[candidates[i]])

        backtrack(target, 0, [])
        return res
