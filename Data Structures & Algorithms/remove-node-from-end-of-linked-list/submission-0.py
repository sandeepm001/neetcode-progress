# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        dummy = curr = head
        while dummy:
            l += 1
            dummy = dummy.next
        p = l-n
        count = 0
        if p==0:
            return head.next
        while curr.next:
            count += 1
            if count==p:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
            
       
        