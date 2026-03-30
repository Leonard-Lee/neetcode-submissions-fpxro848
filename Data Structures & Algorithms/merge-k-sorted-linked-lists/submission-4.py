# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]

        mergedList = lists[0]
        for i in range(1, len(lists)):
            mergedList = self.merge2Lists(mergedList, lists[i])

        return mergedList

        
    def merge2Lists(self, list1, list2):
        dummy = ListNode()
        pre = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                pre.next = list1
                list1 = list1.next
                pre = pre.next
            else:
                pre.next = list2
                list2 = list2.next
                pre = pre.next
        pre.next = list1 or list2
        return dummy.next

        