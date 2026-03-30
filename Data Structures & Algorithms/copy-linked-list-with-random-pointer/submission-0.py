"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # two hash tables
        # random mapping original 3 mapping to orignal 4
        # new mapping original 3 mapping to new 3
        
        if not head: return None

        oldNewDict = {}
        cur = head
        while cur:
            newNode = Node(cur.val, None, None)
            oldNewDict[cur] = newNode
            cur = cur.next
        
        # linking
        cur = head
        while cur:
            newNode = oldNewDict[cur]
            if cur.next == None:
                newNode.next = None
            else:
                newNode.next = oldNewDict[cur.next] 
            
            if cur.random == None:
                newNode.random = None
            else:
                newNode.random = oldNewDict[cur.random]
            cur = cur.next
            
        return oldNewDict[head]
