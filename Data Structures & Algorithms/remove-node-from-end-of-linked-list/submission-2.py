# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        while n:
            n -= 1
            cur = cur.next

        first, sec = dummy, cur
        while cur:
            first = first.next
            cur = cur.next
        first.next = first.next.next
        return dummy.next
        