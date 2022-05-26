class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        palin 일치하지 않을 때
        좌우 한번씩 bound 조정하여 다시확인한다
        좌우 모두 palin 이 아니라면 False, 하나라도 palin 이면 True를 반환한다.
        """
        def check_palindrome(s, i, j):
            """
            i번 인덱스부터 j번 인덱스까지 검사
            """
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True


        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                # 불일치시 좌우 번갈아가면서 체크 -> 하나라도 True 이면 True를 반환
                return check_palindrome(s, l, r-1) or check_palindrome(s, l+1, r)
            l += 1
            r -= 1

        return True


