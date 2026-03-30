# Definition for singly-linked list.
# class ListNode:
#     def __init_(self, val = 0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the length of this linked list
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        # idx = length - n 
        idx = count - n

        # iterate starting from the head
        dummy = ListNode(0, head)

        cur = dummy
        for _ in range(idx):
            cur = cur.next

        cur.next = cur.next.next
        return dummy.next
            