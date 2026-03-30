# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPre = dummy
        while True:
            kNode = self.findKNode(groupPre, k)
            if not kNode: break

            groupNxt = kNode.next
            pre, cur = groupNxt, groupPre.next
            while cur != groupNxt:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            
            # point old head to group next
            oldHead = groupPre.next
            groupPre.next = kNode
            groupPre = oldHead
        
        return dummy.next

    def findKNode(self, node, k) -> Optional[ListNode]:
        cur = node
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

        