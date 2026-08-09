# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a = []
        while head:
            a.append(head.val)
            head = head.next
        
        a.pop(-1*n)

        dummy = ListNode(0)
        curr = dummy

        for x in a:
            curr.next = ListNode(x)
            curr = curr.next
        
        return dummy.next




        