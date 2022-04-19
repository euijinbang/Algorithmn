"""
root에서 가장 먼 leaf root까지의 거리
재귀 DFS로 구현해볼 수 있다. => 작은 문제로 분할한다.
1+MAX(dfs(left), dfs(right))
"""

# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
inorder, dfs 재귀 풀이
"""
class Solution:
    def maxDepth(self, root: Optional[Treeroot]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

"""
preorder, 스택 사용한 dfs 풀이
노드와 레벨을 함께 저장
"""
class Solution:
    def maxDepth(self, root: Optional[Treeroot]) -> int:
        if not root:
            return 0

        res = 0
        stack = [[root, 1]]
        while stack:
            node, level = stack.pop()

            if node:
                res = max(res, level) # 최대깊이 갱신
                stack.append([node.left, level + 1])
                stack.append([node.right, level + 1])
        return res

"""
bfs 풀이
루트는 레벨 1, 내려갈수록 레벨이 증가
"""
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[Treeroot]) -> int:
        if not root:
            return 0  # base-case

        q = deque([root])
        level = 0

        while q:
            # 동일 레벨에 있는 노드들을 탐색한다.
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

