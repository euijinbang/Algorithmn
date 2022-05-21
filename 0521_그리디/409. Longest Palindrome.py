### hash 사용
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # collections.Counter(s) 로 대체 가능
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2      # 몫의 2배를 추가
            if ans % 2 == 0 and v % 2 == 1:  # ans에 홀수값 안더했고, 홀수값이 있다면 1을 추가
                ans += 1
        return ans


### set 사용
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)


### 내풀이 - dict 사용
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        result = 0
        flag = False
        for x in d.values():
            if not x % 2:            # 짝수이면 결과에 추가
                result += x
            else:
                p, q = divmod(x, 2)  # 홀수이면 몫 추가, 나머지 있으면 최종적으로 1을 더한다.
                result += 2 * p
                if q == 1:
                    flag=True
        if flag: result += 1
        return result