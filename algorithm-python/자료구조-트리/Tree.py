"""
이진 트리를 입력받아
전위 순회(preorder traversal),
중위 순회(inorder traversal),
후위순회(postorder traversal)
결과를 출력
"""

"""
이진 자료구조-트리 노드의 개수 N
둘째 줄부터 N개의 줄에 걸쳐 노드와 그의 왼쪽 자식노드, 오른쪽 자식노드
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 
자식 노드가 없는 경우에는 .으로 표현한다.
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# 자료구조-트리 초기화
def init_tree():
    global root

    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n5 = Node(50)
    n6 = Node(60)
    n7 = Node(70)
    n8 = Node(80)

    root = n1
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8


# 전위 순회
def preorder_traverse(node):
    if node == None: return
    print(node.item, end=' -> ')
    preorder_traverse(node.left)
    preorder_traverse(node.right)


# 중위 순회
def inorder_traverse(node):
    if node == None: return
    preorder_traverse(node.left)
    print(node.item, end=' -> ')
    preorder_traverse(node.right)


# 후위 순회
def postorder_traverse(node):
    if node == None: return
    preorder_traverse(node.left)
    print(node.item, end=' -> ')
    preorder_traverse(node.right)


init_tree()
preorder_traverse(root)
