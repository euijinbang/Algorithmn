class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # a - d  ->  a - e  ->  a - f
        # b - d  ->  b - e  ->  b - f ...

        ans = []

        def backtrack(index, path):
            if len(path) == len(digits):
                ans.append(path)
                return

            for i in range(index, len(digits)):
                for letter in dic[digits[i]]:
                    backtrack(i+1, path + letter)


        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        backtrack(0, "")

        if not digits: return []
        return ans
