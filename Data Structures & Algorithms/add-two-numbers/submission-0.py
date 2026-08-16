# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add(head):
            res = []
            while head:
                res.append(str(head.val))
                head = head.next
            return int("".join(res[::-1]))

        x = add(l1)
        y = add(l2)

        z = str(x+y)
        head = dummy= ListNode(0)
        for p in reversed(z):
            head.next = ListNode(int(p))
            head = head.next
        return dummy.next
        