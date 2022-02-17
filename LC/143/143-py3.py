# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. Get length of the ll - O(N)
2. Reverse LL starting at the half point - O(N)
3. Interleave - O(N)
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        size = self.getSize(head)
        if size <= 2:
            return
        
        head_reversed = self.getHalfHead(head, size)
        head_reversed = self.reverseList(head_reversed)
        self.interleave(head, head_reversed)
    
    def getSize(self, head: Optional[ListNode]) -> None:
        count = 0
        node = head
        
        while node:
            count+=1
            node = node.next
            
        return count
    
    def getHalfHead(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        node = head
        half_point = size // 2 + 1 if size % 2 == 1 else size // 2
        
        while half_point > 1:
            node = node.next
            half_point -= 1
        
        head_halved = node.next
        node.next = None
        return head_halved
    
    def reverseList(self, head: Optional[ListNode]) -> None:
        prev_node, node = None, head
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        return prev_node
    
    def interleave(self, upper_head: Optional[ListNode], bottom_head: Optional[ListNode]) -> None:
        upper_node, bottom_node = upper_head, bottom_head
        while bottom_node:
            upper_next, bottom_next = upper_node.next, bottom_node.next
            upper_node.next, bottom_node.next = bottom_node, upper_next
            upper_node, bottom_node = upper_next, bottom_next
