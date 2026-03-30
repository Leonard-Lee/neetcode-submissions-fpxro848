# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
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
        count = 0
        dummy = ListNode()
        dummy.next = head

        cur = head
        pre = dummy
        while cur:
            if count == idx:
                tmp = cur.next
                pre.next = tmp
                break
            count += 1
            pre = cur
            cur = cur.next
        return dummy.next
            