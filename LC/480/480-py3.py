from collections import deque

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k == 0:
            return []
        
        median = []
        window = deque()
        for i in range(len(nums)):
            # print(window)
            self.insert(window, nums[i])
            
            if len(window) > k:
                pos = self.findPosition(window, nums[i-k])
                del window[pos]
            
            if len(window) == k:
                median.append(self.getMedian(window))
        return median
    
    def getMedian(self, window: deque) -> int:
        if len(window) % 2 == 0:
            l, r = len(window) // 2 - 1, len(window) // 2
            return (window[l] + window[r]) / 2
        return window[len(window) // 2]
        
    def insert(self, window: deque, value: int) -> int:
        l, r = 0, len(window) - 1
        while l <= r:
            m = (l + r) // 2
            
            if window[m] == value:
                window.insert(m, value)
                return
            if window[m] < value:
                l = m + 1
            else:
                r = m - 1
        window.insert(l, value)
    
    def findPosition(self, window: deque, value: int) -> int:
        l, r = 0, len(window)-1
        while l <= r:
            m = (l + r) // 2
            
            if window[m] == value:
                return m
            if window[m] < value:
                l = m + 1
            else:
                r = m - 1
        return -1
