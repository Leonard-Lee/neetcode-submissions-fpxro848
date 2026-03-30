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
            kNode = self.locateKNode(groupPre, k)
            if not kNode: break
            
            nextGroup = kNode.next
            pre, cur = nextGroup, groupPre.next
            while cur != nextGroup:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            tmp = groupPre.next 
            groupPre.next = kNode
            groupPre = tmp

        return dummy.next
        
    def locateKNode(self, node, k):
        while node and k > 0:
            k -= 1
            node = node.next
        return node
    

        