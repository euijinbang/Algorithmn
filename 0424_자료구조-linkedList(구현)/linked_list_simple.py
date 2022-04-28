#Node 정의
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#Node 생성해보기(data = 1)
node1 = Node(1)

#Node의 값과 포인터 출력하기
print(node1.data)
print(node1.next)

#Node 연결하기
node1 = Node(1)
node2 = Node(3)
node1.next = node2
#가장 맨 앞 Node를 알기 위해 head 지정
head = node1

#node1을 통해 연결한 결과 확인(밑에 2줄은 동일한 결과를 가리킨다)
print(node1.next.data)
print(node2.data)
