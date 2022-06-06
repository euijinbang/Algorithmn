# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        a, b => pointer
        """
        a = headA   #ListNode
        b = headB   #ListNode

        while a != b:
            a = a.next if a else headB  #beginning of headB
            b = b.next if b else headA  #beginning of headA

        return a