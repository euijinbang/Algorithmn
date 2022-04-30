#방법1. 노드자체를 스택에 좌우로 쌓으면서 비교
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root: return True
        # 노드 자체를 쌍으로 담아서 left.left 노드와 right.right, left.right과 right.left를 비교
        stack = deque([(root.left, root.right)])
        while stack:
            l, r = stack.pop()
            if not l and not r:     # 양쪽 다 비었으면 다시 pop
                continue
            if not l or not r:      # 한쪽이라도 비었으면 비대칭
                return False
            if l.val != r.val:      # 값 비교
                return False

            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True

#방법2. (내풀이)값을 저장해서 한 level마다 비교

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        q = deque()
        q.append(root)
        flag = True
        while q:
            siblings_l, siblings_r = [], []

            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                    siblings_l.append(cur.left.val)
                else:
                    siblings_l.append("left_null")

                if cur.right:
                    q.append(cur.right)
                    siblings_r.append(cur.right.val)
                else:
                    siblings_r.append("right_null")

            if siblings_l != siblings_r[::-1]:
                flag = False
        return flag