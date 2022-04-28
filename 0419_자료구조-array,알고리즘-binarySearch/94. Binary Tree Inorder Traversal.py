"""
inorder의 경우 root에서 시작(중간 - 좌 - 우)
왼쪽 자식노드 - 부모노드 - 오른쪽 자식노드 순으로 탐색한다.
- 재귀함수로 구현한다.
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            # 더이상 왼쪽/오른쪽 자식노드가 없으면 리턴한다.
            if not root:
                return
            inorder(root.left)
            res.append(root.val)

            inorder(root.right)

        inorder(root)
        return res