class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # this is the key
        second = slow.next
        slow.next = None
        
        # reverse the second part
        pre = None
        while second:
            n = second.next
            second.next = pre
            pre = second
            second = n

        # rearrange 
        first, second = head, pre
        dummy = ListNode()
        i = 0
        cur = dummy
        while first and second:
            if i % 2 == 0:
                cur.next = first
                first = first.next
            else:
                cur.next = second
                second = second.next
            cur = cur.next
            i += 1
        cur.next = first or second