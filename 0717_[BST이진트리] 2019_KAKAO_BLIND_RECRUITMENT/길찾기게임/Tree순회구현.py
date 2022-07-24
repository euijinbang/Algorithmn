class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node


# 전위순회(Preorder) 자기자신 -> 왼 -> 오
def preOrder(node):
    print(node.data, end='')
    if node.left_node is not None:
        preOrder(tree[node.left_node])  # dict의 value가 노드
    if node.right_node is not None:
        preOrder(tree[node.right_node])


# 중위순회(Inorder) 왼 -> 자기자신 -> 오
def inOrder(node):
    if node.left_node is not None:
        inOrder(tree[node.left_node])  # dict의 value가 노드
    print(node.data, end='')
    if node.right_node is not None:
        inOrder(tree[node.right_node])


# 후위순회(Postorder) 왼 -> 오 -> 자기자신
def postOrder(node):
    if node.left_node is not None:
        postOrder(tree[node.left_node])  # dict의 value가 노드
    if node.right_node is not None:
        postOrder(tree[node.right_node])
    print(node.data, end='')


# 트리 구현
n = int(input())

# dictionary 자료구조로 구현
tree = {}

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

print('---------------------------------')

# 시작노드 입력하면 DFS 시작
preOrder(tree['A'])
print()
inOrder(tree['A'])
print()
postOrder(tree['A'])
