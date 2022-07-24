# 파이썬 재귀 limit이 1000이라 늘려야
import sys
sys.setrecursionlimit(10**6)


class BinarySearchTreeNode:
    """
    x 좌표 => 비교기준
    y 좌표 따로
    index 따로
    """
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

    def add_child(self, x, y, idx):
        if x == self.x:
            return

        # 왼쪽으로
        if x < self.x:
            if self.left:
                self.left.add_child(x, y, idx)
            else:
                self.left = BinarySearchTreeNode(x, y, idx)

        # 오른쪽으로
        if x > self.x:
            if self.right:
                self.right.add_child(x, y, idx)
            else:
                self.right = BinarySearchTreeNode(x, y, idx)

    def preOrderTraversal(self):
        elements = []
        elements.append(self.idx)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        return elements

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.idx)
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.idx)
        return elements


def build_tree(elements):
    x, y, idx = elements[0][0], elements[0][1], elements[0][2]
    root = BinarySearchTreeNode(x, y, idx)

    for s in range(1, len(elements)):
        x, y, idx = elements[s][0], elements[s][1], elements[s][2]
        root.add_child(x, y, idx)

    return root


# if __name__ == '__main__':
def solution(nodeinfo):

    """
    (x, y, idx) 로 구성된 배열
    """
    # nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
    n = len(nodeinfo)
    numbers = []
    for i in range(n):
        numbers.append((nodeinfo[i][0], nodeinfo[i][1], i+1))

    # numbers y좌표 높은 순, x 좌표 낮은 순 정렬 => numbers[0] 이 트리 시작점
    numbers.sort(key=lambda x: (-x[1], x[0]))

    # 1. 트리를 만들쟝
    numbers_tree = build_tree(numbers)

    # 2. 순회를 하쟝
    # print(numbers_tree.preOrderTraversal())
    # print(numbers_tree.inOrderTraversal())
    # print(numbers_tree.postOrderTraversal())

    answer = [numbers_tree.preOrderTraversal(), numbers_tree.postOrderTraversal()]
    return answer
