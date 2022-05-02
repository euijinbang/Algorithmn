#흠....어렵네...다시풀어야겠다.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #바로 전 인덱스값이 현재 인덱스값과 같으면 현재 브랜치를 선택하지 않는다.
        candidates.sort()
        res = []
        def backtrack(cur, index, target):
            if target <= 0:
                if target == 0:
                    res.append(cur.copy())
                    return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i+1, target-candidates[i])
                cur.pop()

        backtrack([], 0, target)
        return res
