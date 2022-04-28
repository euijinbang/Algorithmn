# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 갯수를 세서 2로 나누어 구하는 방법
        #         dummy = ListNode()
        #         tail = dummy
        #         tail.next = head
        #         count = -1
        #         while tail:
        #             count += 1
        #             tail = tail.next

        #         num = 0
        #         while head:
        #             num += 1
        #             if num == count // 2 + 1:
        #                 break
        #             head = head.next

        #         return head

        #Floyd's Tortoise and Hare
        #T는 H보다 2배 빠르므로 T 또는 T.next 가 null 일때 H가 중앙이다.
        t = head
        h = head

        while t and t.next:
            t = t.next.next
            h = h.next

        return h
