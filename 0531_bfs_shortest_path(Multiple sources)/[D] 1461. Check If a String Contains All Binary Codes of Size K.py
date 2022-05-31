class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1. s의 substring을 set으로 구한다.(연속된 k개의 수 말하는 것)
        # 2. 1<<k 로 k개로 만들 수 있는 바이너리 코드 갯수를 구한다.
        # 3. 두 갯수가 다르면 False
        subs = set()
        for i in range(0, len(s)-k+1):
            subs.add(s[i:i+k])

        return len(subs) == (1 << k)