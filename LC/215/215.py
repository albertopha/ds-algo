"""
======================================================
Test cases:
           p
[3,2,1,4,5,6], k = 2
       ^
======================================================
Brute force:
1. Sort the array descending order -- O(NlogN)
2. return k - 1th element

Time: O(NlogN)
Space: O(NlogN)
======================================================
Optimal (Priority Queue):
1. Heapify the arr --- O(N)
2. Find the kth largest --- O(N)

Time: O(N)
Space: O(N)
======================================================
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k > len(nums):
            return -1
        
       return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
    
    def heap(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    
    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[end] = nums[end], nums[i]
        return i
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        pivot = self.partition(nums, start, end)
        
        # Search right
        if pivot == k:
            return nums[k]
        
        if k < pivot:
            return self.quickSelect(nums, start, pivot - 1, k)
        return self.quickSelect(nums, pivot + 1, end, k) """
======================================================
Test cases:
           p
[3,2,1,4,5,6], k = 2
       ^
======================================================
Brute force:
1. Sort the array descending order -- O(NlogN)
2. return k - 1th element

Time: O(NlogN)
Space: O(NlogN)
======================================================
Optimal (Priority Queue):
1. Heapify the arr --- O(N)
2. Find the kth largest --- O(N)

Time: O(N)
Space: O(N)
======================================================
"""

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or k > len(nums):
            return -1
        
       return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
    
    def heap(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    
    def partition(self, nums, start, end):
        pivot = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        nums[i], nums[end] = nums[end], nums[i]
        return i
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        pivot = self.partition(nums, start, end)
        
        # Search right
        if pivot == k:
            return nums[k]
        
        if k < pivot:
            return self.quickSelect(nums, start, pivot - 1, k)
        return self.quickSelect(nums, pivot + 1, end, k) 
