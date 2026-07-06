"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # three passes
    # 1. clone new nodes
    # 2. set up random pointers
    # 3. decouple
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        cur = head
        while cur:
            newNode = Node(cur.val)
            nxt = cur.next
            cur.next = newNode
            newNode.next = nxt
            cur = nxt

        # set up random pointers
        cur = head
        while cur:
            # this is the key
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next

            cur = copy.next

        # decouple
        newHead = head.next
        cur = head
        while cur:
            # this is the key
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next

            cur = cur.next

        return newHead
        