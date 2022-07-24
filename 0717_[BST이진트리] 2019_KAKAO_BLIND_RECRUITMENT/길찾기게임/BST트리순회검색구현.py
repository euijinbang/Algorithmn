class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        # 왼쪽으로
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        # 오른쪽으로
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements

    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)
        return elements

    def search(self, val):
        if self.data == val:    # val 을 찾으면 True 리턴
            return True

        if val < self.data:
            # val 이 아마도 left subtree에 있을 것
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # val 이 아마도 right subtree에 있을 것
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.preOrderTraversal())
    print(numbers_tree.inOrderTraversal())
    print(numbers_tree.postOrderTraversal())

    countries = ["UK", "Pakistan", "Germany", "USA", "China", "USA"]
    country_tree = build_tree(countries)
    print("UK is in list?", country_tree.search("UK"))
    print("Sweden is in list?", country_tree.search("Sweden"))
