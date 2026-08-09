# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = [], []

        while l1:
            a.append(str(l1.val))
            l1 = l1.next

        num1 = int(''.join(a[::-1]))

        while l2:
            b.append(str(l2.val))
            l2 = l2.next

        num2 = int(''.join(b[::-1]))

        t = int(num1) + int(num2)
        t = list(str(t)[::-1])
        t = list(map(int, t))       


        def list_to_linked(arr):
            dummy = ListNode(0)
            curr = dummy

            for x in arr:
                curr.next = ListNode(x)
                curr = curr.next

            return dummy.next
        
        return list_to_linked(list(t))

        