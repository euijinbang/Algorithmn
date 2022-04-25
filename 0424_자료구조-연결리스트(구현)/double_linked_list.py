class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class DoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def add_first(self, data):
        new_node = Node(data)

        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

        self.d_size += 1

    def add_last(self, data):
        new_node = Node(data)

        new_node.prev = self.tail.prev
        new_node.next = self.tail

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1

    def insert_after(self, data, node):
        new_node = Node(data)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1

    def insert_before(self, data, node):
        new_node = Node(data)

        new_node.next = node
        new_node.prev = node.prev

        node.prev.next = new_node
        node.prev = new_node

        self.d_size += 1

    def search_forward(self, target):
        cur = self.head.next

        while cur is not self.tail:
            if cur.data == target:
                return cur
            cur = cur.next
        return None

    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1


def show_list(dlist):
    print('data size : {}'.format(dlist.size()))
    cur = dlist.head.next
    while cur is not dlist.tail:
        print(cur.data, end = " ")
        cur = cur.next
    print()


if __name__ == "__main__":
    dlist = DoubleLinkedList()
    print("데이터 삽입")
    dlist.add_first(1)
    dlist.add_first(2)
    dlist.add_last(3)
    dlist.add_last(5)
    dlist.insert_after(7, dlist.search_forward(3))
    show_list(dlist)

    print("데이터 탐색")
    target = 3
    res = dlist.search_forward(target)
    if res:
        print("데이터 {} 탐색 성공".format(res.data))
    else:
        print("데이터 {} 탐색 실패".format(target))

    print("데이터 삭제")
    dlist.delete_node(dlist.search_forward(5))
    show_list(dlist)
