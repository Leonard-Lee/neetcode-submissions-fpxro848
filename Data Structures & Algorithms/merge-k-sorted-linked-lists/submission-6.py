# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None

        minHeap = []
        dummy = ListNode()
        cur = dummy

        for l in lists:
            minHeap.append(l)
        
        heapq.heapify(minHeap)

        while minHeap:
            minNode = heapq.heappop(minHeap)
            if minNode.next:
                heapq.heappush(minHeap, minNode.next)
            cur.next = minNode
            cur = minNode

        return dummy.next