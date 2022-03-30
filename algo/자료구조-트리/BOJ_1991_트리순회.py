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
import sys
sys.stdin = open("../input_1991.txt")


# 전위 순회
def preorder(root):
    if root != ".":
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])


# 중위 순회
def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])


# 후위 순회
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


N = int(input())
tree = {}

for i in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder("A")
print()
inorder("A")
print()
postorder("A")
