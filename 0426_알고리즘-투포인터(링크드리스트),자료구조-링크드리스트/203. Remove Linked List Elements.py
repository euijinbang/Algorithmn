# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # 제일 앞단 노드 추가
        dummy = ListNode(next=head)
        # 2 pointers : delete를 위한 prev 포인터와 현재값 확인을 위한 cur 포인터
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next
