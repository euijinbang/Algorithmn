class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        ss = []

        for i in range(len(s)):
            diff = ord(s[i]) - ord(t[i])

            #문자가 d에 있으면 사용, 없으면 만든다.
            if s[i] in d:
                if d[s[i]] != diff:
                    return False
            else:
                #서로 다른 문자가 같은 문자로 치환 불가
                if chr(ord(s[i]) - diff) in ss:
                    return False
                d[s[i]] = diff
                ss.append(t[i])

        return True
