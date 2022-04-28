# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 풀이 1. 돌면서 노드를 hashSet 에 저장(data는 중복될 수 있기에 node object를 저장한다.) [O(n)], [O(n)]
        # head를 옮겨가면서 마지막 노드의 next가 Null을 가리키면 Cycle이 없다.
        # 마지막 노드의 next가 Null을 가리키지않고, hashSet에 있는 노드를 또다시 가리키면 Cycle이 있다.

        nodeSet = set()

        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next

        return False

        # 풀이 2. time[O(n)] space(memory)[O(1)] Floyd's Tortoise and Hare
        # slow, fast 포인터를 옮겨가다보면 사이클이 있다면 언젠가 반드시 만난다.

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
