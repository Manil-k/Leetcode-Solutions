# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        for l in lists:
            while l:
                temp.append(l.val)
                l = l.next
        
        temp.sort()

        dummy = ListNode(0)
        curr = dummy

        for x in temp:
            curr.next = ListNode(x)
            curr = curr.next
        
        return dummy.next
            
            
        