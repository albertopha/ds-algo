# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        
        end = head
        while n > 0:
            end = end.next
            n -= 1
            
        if not end:
            return head.next
        
        end = end.next
        start = head
        while end:
            start = start.next
            end = end.next
        
        if start.next:
            start.next = start.next.next
        
        return head
        
