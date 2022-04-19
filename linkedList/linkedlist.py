class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# node 생성
node1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)

# node 연결
node1.next = node2
node2.next = node3
node3.next = node4

# head 지정
head = node1

node = head
while node.next:
    print(node.data)
    node = node.next

print(node.data)