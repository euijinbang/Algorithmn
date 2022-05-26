class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #@[[2,2,3],[2,3,2],[3,2,2],[7]] => [[2,2,3],[7]]
        ans = []
        def backtrack(comb, target, start):
            if target == 0:
                ans.append(comb.copy())
                return
            if target < 0:
                return

            # 시작인덱스 조정
            for idx in range(start, len(candidates)):
                target -= candidates[idx]
                comb.append(candidates[idx])
                backtrack(comb, target, idx)
                target += candidates[idx]
                comb.pop()

        backtrack([], target, 0)

        return ans