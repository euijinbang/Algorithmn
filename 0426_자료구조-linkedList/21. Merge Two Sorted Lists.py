# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 리스트의 head 역할을 하는 dummy node 생성. head.next를 리턴하면 된다.
        dummy = ListNode()
        # dummy의 마지막까지 움직이는 포인터
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # 남은 잔여 연결리스트를 연결
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next