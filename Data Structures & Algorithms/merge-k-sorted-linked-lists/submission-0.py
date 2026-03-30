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

        ret = ListNode(0, lists[0])
        for i in range(1, len(lists)):
            print(i)
            self.mergeTwoLists(ret, lists[i])
        return ret.next

    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        head = list1
        list1 = list1.next

        pre = head
        while list1 and list2:
            print("list1 val: " + str(list1.val) + " ; list2 val: " + str(list2.val))
            if list1.val <= list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next

        pre.next = list1 or list2
        print("head val: " + str(head.val))


        

    
        