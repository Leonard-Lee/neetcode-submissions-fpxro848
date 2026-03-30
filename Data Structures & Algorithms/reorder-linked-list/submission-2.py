# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse the second part
        pre = None
        while second:
            tmp = second.next
            second.next = pre
            pre = second
            second = tmp
        
        # merage first part and second part
        h1, h2 = head, pre
        while h1 and h2:
            tmp1 = h1.next
            tmp2 = h2.next
            h1.next = h2
            h2.next = tmp1
            h1 = tmp1
            h2 = tmp2

        