# - 이진 검색 트리의 항목 찾기
# - 새 항목 삽입하기
# - 항목 삭제하기
class TreeNode:
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None
        self.__parent = None

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def parent(self):
        return self.parent

    @parent.setter
    def parent(self, parent):
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur):
        if not cur:
            return
        print(cur.key)
        self.preorder_traverse(cur.left)
        self.preorder_traverse(cur.right)

    # key가 정렬된 상태로 출력
    def inorder_traverse(self, cur):
        if not cur:
            return
        self.inorder_traverse(cur.left)
        print(cur.key)
        self.inorder_traverse(cur.right)

    # 노드 삽입 연산
    def insert(self, key):
        # 새로운 노드 생성 후 parent, cur 포인터를 바꿔가면서 진행
        # cur은 루트에서 시작한다.

        new_node = TreeNode(key)
        cur = self.root

        # 루트가 없으면 만들어준다.
        if not cur:
            self.root = new_node
            return

        # 반복 진행
        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                # cur를 왼쪽 자식노드로 옮기고 비어있으면 그곳에 배치(cur는 None이므로 parent 사용)
                if not cur:
                    parent.left = new_node
                    return

            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return

    # search
    # cur 노드를 루트부터 시작, cur.key와 target을 변경하면서 cur를 움직여준다.
    def search(self, target):
        cur = self.root

        while True:
            try:
                if cur.key == target:
                    print("found {}".format(cur.key))
                    return cur
                elif cur.key > target:
                    cur = cur.left
                elif cur.key < target:
                    cur = cur.right
            except:
                return "not able to find"


bst = BST()

bst.insert(6)
bst.insert(5)
bst.insert(1)
print(bst.search(2))
bst.inorder_traverse(bst.get_root())
