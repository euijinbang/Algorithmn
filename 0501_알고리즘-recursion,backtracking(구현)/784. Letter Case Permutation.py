class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        # 알파벳이면 a, A 두 갈래로 나누어서 dfs, 숫자면 dfs 진행
        res = []
        def backtrack(sub, i):
            if len(sub) == len(s):
                res.append(sub)     # 문자열이라 copy 안해도 됨
                return

            if s[i].isalpha():
                sub += s[i].lower()
                backtrack(sub, i+1)
                sub = sub[:-1]

                sub += s[i].upper()
                backtrack(sub, i+1)
                sub = sub[:-1]

            else:
                sub += s[i]
                backtrack(sub, i+1)
                sub = sub[:-1]

        backtrack("", 0)
        return res


        #방법2, 축약형- 파라미터에 더하면 return시 이전으로 돌아간다.
        class Solution:
            def letterCasePermutation(self, s: str) -> List[str]:
                # 알파벳이면 a, A 두 갈래로 나누어서 dfs, 숫자면 dfs 진행
                res = []
                def backtrack(sub, i):
                    if len(sub) == len(s):
                        res.append(sub)     # 문자열이라 copy 안해도 됨
                        return

                    if s[i].isalpha():
                        backtrack(sub + s[i].lower(), i+1)
                        backtrack(sub + s[i].upper(), i+1)
                    else:
                        backtrack(sub + s[i], i+1)

                backtrack("", 0)
                return res