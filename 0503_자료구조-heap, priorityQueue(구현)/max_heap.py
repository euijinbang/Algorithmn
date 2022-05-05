"""
힙이란? 배열로 구현한 완전 이진 트리
=> 힙 정렬과 우선순위 큐에 쓰인다.
"""
class Element:
    def __init__(self, key):
        self.key = key

class MaxHeap:
    MAX_ELEMENTS = 100      #힙의 크기
    def __init__(self):
        self.arr = [None for i in range(self.MAX_ELEMENTS+1)]   #요소를 저장할 배열
        self.heapsize = 0   #키의 개수

    def is_empty(self):
        """
        힙사이즈가 0이면 빈 힙이다.
        """
        if self.heapsize == 0:
            return True
        return False

    def is_full(self):
        """
        키의 개수가 힙의 크기 이상이면 다 찼다고 판단
        """
        if self.heapsize >= self.MAX_ELEMENTS:
            return True
        return False

    def parent(self, idx):
        """
        부모 노드의 인덱스 반환
        """
        return idx // 2

    def left(self, idx):
        """
        왼쪽 자식 노드의 인덱스 반환
        """
        return idx * 2

    def right(self, idx):
        """
        오른쪽 자식 노드의 인덱스 반환
        """
        return idx * 2 + 1

    def push(self, item):
        """
        삽입
        1. 완전이진트리가 되도록 노드를 추가한다.
        2. 최대힙 특성을 이룰 때 까지(해당 키가 부모 키보다 작거나 같을 때 까지) swap한다.
        """
        if self.is_full():
            raise IndexError("the heap is full!")

        # 완전이진트리를 유지하기 위해
        # 마지막 원소의 다음 인덱스에 추가한다.
        self.heapsize += 1
        cur_idx = self.heapsize

        # cur_idx가 루트가 아니고 item의 key가 cur_idx의 부모의 key보다 크면
        while cur_idx != 1 and item.key > self.arr[self.parent(cur_idx)].key:
            # 1.현재 위치 원소에 부모원소를 넣는다.
            # 2.cur_idx를 부모 인덱스로 바꾼다.
            # 3.이것을 반복한다.
            self.arr[cur_idx] = self.arr[self.parent(cur_idx)]
            cur_idx = self.parent(cur_idx)

        # 4.cur_idx가 루트이거나 또는 item의 key가 cur_idx의 부모의 key보다 크면 현재 인덱스 위치에 새 요소를 넣는다.
        self.arr[cur_idx] = item

    def pop(self):
        """
        꺼내기
        1. 루트 인덱스의 요소를 꺼낸다(pop[1])
        2. 최대힙 특성이 깨졌으므로
            1) 완전 이진트리로 만든다. 마지막 인덱스 요소를 루트로 이동!
            2) 어떤 노드의 키가 자식 노드의 키보다 작지 않도록 한다.
        """
        if self.is_empty():
            return None

        rem_elem = self.arr[1]  # 삭제 후 반환될 원소를 저장해둔다.

        temp = self.arr[self.heapsize]  # 0. 맨 마지막 원소를 temp 담아둔다.
        self.heapsize -= 1

        cur_idx = 1     # 루트에서 시작
        # 0. root의 왼쪽 자식부터 자식으로 잡는다.
        child = self.left(cur_idx)

        # 리프 노드면 종료한다.
        while child <= self.heapsize:
            # 1. 오른쪽 자식이 있고(완전이진트리 특성 참고), 오른쪽 자식의 key가 왼쪽 자식의 key보다 크면
            #    child(index)를 오른쪽 자식(index)으로 바꾼다.
            # 2. temp의 key가 자식요소의 key보다 크거나 같으면 반복문을 빠져나온다.
                    # 5. 반복문을 빠져나오면 cur_idx 위치에 temp 원소를 넣고 삭제한 원소를 반환한다.
            # 3. 그렇지 않다면, key가 큰 자식의 원소를 부모(cur_idx)에 넣고, cur_idx를 자식으로 옮긴다.
            # 4. cur_idx의 왼쪽 자식을 자식으로 잡는다.
            if child < self.heapsize and self.arr[self.right(cur_idx)].key > self.arr[self.left(cur_idx)].key:
                child = self.right(cur_idx)

            if temp.key >= self.arr[child].key:
                break

            self.arr[cur_idx] = self.arr[child]
            cur_idx = child
            child = self.left(cur_idx)

        self.arr[cur_idx] = temp
        return rem_elem


########################################################
def print_heap(h):
    for i in range(1, h.heapsize+1):
        print("{}".format(h.arr[i].key, end=' '))
    print()


if __name__ == "__main__":
    h = MaxHeap()
    h.push(Element(2))
    h.push(Element(14))
    h.push(Element(9))
    h.push(Element(11))
    h.push(Element(6))
    h.push(Element(8))

    print_heap(h)

    while not h.is_empty():
        rem = h.pop()
        print("popped item is {}".format(rem.key))
        print_heap(h)
