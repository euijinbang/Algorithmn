"""
if 조건A or 조건B 라고 했을 때
오류구문이 조건B 위치에 있을 경우
조건 A의 구문이 True이면 조건 B는 판단하지 않기 때문에
에러가 발생하지 않는다.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # ["ab", "a"]

        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                # 조건순서 주의
                # i == len(s) 가 맞으면 뒤는 검사하지 않으므로 => index error 발생하지 않음.
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res