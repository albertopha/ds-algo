"""
===============================================================
Brute force:
1. Mimic insertion sort when adding a number to the array

Time: O(N^2) where O(N^2) from addNum and O(1) for findMedian
Space: O(N)
===============================================================
Sub-optimal (sort):
1. Mimic insertion sort by using binary search

Time: O(NlogN) from addNum and O(1) from findMedian
Space: O(N) from the sorted array
===============================================================
Sub-optimal (sort):
1. Sort the array everytime either from findMedian or addNum

Time: O(NlogN) from sort
Space: O(NlogN) from sort
===============================================================
Optimal (two heaps):
1. Use two heaps:
    a. one heap is a max heapthat contains the lower values.
    b. the other is a min heap that has the higher values.

2. Add the new value to the min heap.
3. If the sizes of these two heaps are differ by more than 1,
    rebalance the heaps.
4. Find median:
    a. if the sizes of two heaps are equal, peek from both heaps
        and calculate the median
    b. else, peek the value from the heap that has larger size.

Time: O(logN)
Space: O(N)
===============================================================
"""
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lowers = [] # max heap
        self.highers = [] # min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.lowers or num <= -self.lowers[0]:
            heapq.heappush(self.lowers, -num)
        else:
            heapq.heappush(self.highers, num)
        
        if abs(len(self.lowers) - len(self.highers)) >= 2:
            self.rebalance()
        
    
    def rebalance(self):
        larger = self.lowers if len(self.lowers) >= len(self.highers) else self.highers
        smaller = self.lowers if len(self.lowers) < len(self.highers) else self.highers
        heapq.heappush(smaller, -heapq.heappop(larger))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.lowers) == len(self.highers):
            mid1, mid2 = -self.lowers[0], self.highers[0]
            return (float(mid1) + float(mid2)) / 2
        
        return -self.lowers[0] if len(self.lowers) > len(self.highers) else self.highers[0]
        
#         if not self.nums:
#             return 0
        
#         mid = len(self.nums) // 2
#         if len(self.nums) % 2 == 0:
#             return (float(self.nums[mid-1]) + float(self.nums[mid])) / 2
        
#         return self.nums[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 
