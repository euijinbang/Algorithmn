# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #방법1. bfs풀이
        if not root:
            return 0

        depth = 0
        q = deque()
        q.append(root)

        while q:
            depth += 1  #한 level 돌릴 때 마다 깊이 증가
            for _ in range(len(q)):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)


        return depth


        #방법2. dfs풀이
        if not root:
            return 0

        md = 0
        q = deque()
        q.append((root, 1))

        while q:
            cur, depth = q.pop()


            if depth > md:
                md = depth

            for _ in range(1):
                if cur.left:
                    q.append((cur.left, depth + 1))
                if cur.right:
                    q.append((cur.right, depth + 1))

        return md


        #방법3. recursive
        def dfs(root, depth):
            if not root: return depth

            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


        #방법4. 재귀-내풀이
        #리턴값에 depth를 넣어주면 global 처리를 할 필요가 없다
        global md
        md = 0
        def maxDep(node, depth):
            global md
            if not node:
                depth -= 1
                return
            md = max(md, depth)
            maxDep(node.left, depth + 1)
            maxDep(node.right, depth + 1)
            return md

        result = maxDep(root, 1)
        return result
