"""
left = maxHeap
right = minHeap
"""
import heapq

class MedianFinder:

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        if not self.right_heap or\
            not self.left_heap or\
            self.right_heap[0] <= num:
            heapq.heappush(self.right_heap, num)
        else:
            heapq.heappush(self.left_heap, -num)
        self.balanceHeaps()

    def findMedian(self) -> float:
        if not self.right_heap and not self.left_heap:
            return 
        
        peek_right = self.right_heap[0] if self.right_heap else None
        peek_left = -self.left_heap[0] if self.left_heap else None 
        
        if len(self.left_heap) == len(self.right_heap):
            return (peek_left + peek_right) / 2
        if len(self.left_heap) > len(self.right_heap):
            return peek_left
        return peek_right
    
    def balanceHeaps(self):
        if len(self.left_heap) + 1 < len(self.right_heap):
            num = heapq.heappop(self.right_heap)
            heapq.heappush(self.left_heap, -num)
        elif len(self.left_heap) > len(self.right_heap) + 1:
            num = -heapq.heappop(self.left_heap)
            heapq.heappush(self.right_heap, num)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
