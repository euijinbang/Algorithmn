# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # bfs풀이

        if not root: return []

        res = []

        q = deque([root])

        while q:
            vals = []
            for _ in range(len(q)):     #q 의 길이만큼 반복 == level의 노드 수만큼 반복
                cur = q.popleft()
                vals.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(vals)

        return res
