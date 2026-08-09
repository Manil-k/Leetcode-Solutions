# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        a, b = [], []

        while list1:
            a.append(list1.val)
            list1 = list1.next
        
        while list2:
            b.append(list2.val)
            list2 = list2.next

        
        a = a + b
        a.sort()

        dummy = ListNode(0)
        curr = dummy

        for x in a:
            curr.next = ListNode(x)
            curr = curr.next
        
        return dummy.next
        
        