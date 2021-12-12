# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        pq = self.getPQ(lists)
        return self.buildLinkedList(pq)
    
    def buildLinkedList(self, pq: List[int]) -> Optional[ListNode]:
        head = ListNode(0)
        tmp = head
        while pq:
            tmp.next = ListNode(heapq.heappop(pq))
            tmp = tmp.next
        return head.next
    
    def getPQ(self, lists: List[Optional[ListNode]]) -> List[int]:
        pq = []
        for node in lists:
            tmp = node
            while tmp:
                heapq.heappush(pq, tmp.val)
                tmp = tmp.next
        return pq
                
