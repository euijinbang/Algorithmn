class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        1. 큰 수부터 정렬
        2. 더 작은 수의 k-value == index
        """
        people.sort(key=lambda x:(-x[0], x[1]))

        ans = []
        for p in people:
            ans.insert(p[1], p)

        return ans