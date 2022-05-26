class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        정렬 후 child, cookie 인덱스 이동, child 인덱스 반환 (==만족한 아이수)
        """
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s) :
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i