class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        for i in range(len(s)):
            #앞선 문자가 다르게 치환되는 경우
            if s[i] in sd and sd[s[i]] != t[i]:
                return False
            #뒤의 문자가 중복 치환되는 경우
            if t[i] in td and td[t[i]] != s[i]:
                return False

            sd[s[i]] = t[i]
            td[t[i]] = s[i]

        return True
