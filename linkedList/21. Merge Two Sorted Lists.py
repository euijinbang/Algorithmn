# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 더미 연결리스트 생성
        dummy = ListNode()

        # tail 설정
        tail = dummy

        # 현재 노드 비교하면서 작은 수를 tail 다음에 담고, 현재 링크드 리스트 갱신
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # 남은 링크드리스트 연결
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        # dummy 뒤의 링크드리스트 반환
        return dummy.next