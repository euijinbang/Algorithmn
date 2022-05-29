class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
        hashSet
        - 교집합 없으면 True ...  x1.isdisjoint(x2)
        - 교집합 찾기 ... x1 & x2
        - 차집합 찾기 ... x1 - x2
        - 합집합 찾기 ... x1 | x2
        - 여집합 찾기 ... x1 ^ x2
        """
        n = len(words)
        max_len = 0
        hashSet = [set(words[i]) for i in range(n)]

        for i in range(0, n-1):
            for j in range(i+1, n):
                # 두 집합의 교집합 없으면 진행
                # x1.isdisjoint(x2) returns True if x1 and x2 have no elements in common
                # if not hashSet[i] & hashSet[j]:
                if hashSet[i].isdisjoint(hashSet[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len