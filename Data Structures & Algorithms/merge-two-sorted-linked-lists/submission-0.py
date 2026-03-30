class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        cur = dummyHead

        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                cur = head1
                head1 = head1.next
            else:
                cur.next = head2
                cur = head2
                head2 = head2.next
        if head1:
            cur.next = head1
        else: 
            cur.next = head2
            
        return dummyHead.next

        