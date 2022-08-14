from collections import defaultdict

class Solution(object):
    def edgeScore(self, edges):
        """
        :type edges: List[int]
        :rtype: int
        """
        score = defaultdict(int)
        for i, edge in enumerate(edges):
            score[edge] += i

        max_val = max(score.values())
        for i in range(len(edges)):
            # key 를 돌면서 발견시 바로 반환 => 작은 것부터 찾아진다.
            if score[i] == max_val:
                return i
