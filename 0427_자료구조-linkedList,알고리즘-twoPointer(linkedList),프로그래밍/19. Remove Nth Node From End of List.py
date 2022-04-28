# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #         # 방법1. 멈추는 번째를 계산해서 구하기
        #         # n번째 == 전체 갯수 - n + 1번째
        #         dummy = ListNode()
        #         tail = dummy
        #         tail.next = head
        #         count = -1
        #         while tail:
        #             count += 1
        #             tail = tail.next

        #         stop_cnt = count - n + 1

        #         dummy2 = ListNode()
        #         dummy2.next = head
        #         # dummy부터 시작하는 pointer를 정의! => 이부분이 놓친 부분..!
        #         pointer = dummy2
        #         cnt = -1
        #         while pointer:
        #             cnt += 1
        #             # 멈추는 노드의 이전 노드를 찾아서 next를 바꾼다.
        #             if cnt == stop_cnt - 1:
        #                 pointer.next = pointer.next.next
        #             else:
        #                 pointer = pointer.next

        #         return dummy2.next


        #방법2. dummy에서 시작하는 left 포인터, head에서 시작하는 right 포인터를 이용(left의 위치가 멈추는 위치 이전이어야 하므로)
        #두 포인터 간격을 n만큼 벌리고 하나씩 이동하다가 right가 null이 되면 그때의 left.next를 바꿔준다.
        dummy = ListNode(next=head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next