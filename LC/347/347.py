import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k > len(nums):
            return []
        
        counter = Counter(nums)
        sets = []
        for num, count in counter.items():
            sets.append((count, num))
        
        self.quickSelect(sets, 0, len(sets)-1, k)
        print(sets)
        result = []
        for count, num in sets[len(sets)-k:]:
            result.append(num)
        return result

    
    def minHeap(self, nums, k, counter):
        heap = []
        for num, counter in counter.items():
            heappush(heap, (-counter, num))
       
        result = []
        while k > 0:
            result.append(heappop(heap)[1])
            k -= 1
            
        return result
    
    def quickSelect(self, sets, start, end, k):
        if start >= end:
            return
        
        pivot = self.partition(sets, start, end)
        
        if len(sets) - k == pivot:
            return
        
        if len(sets) - k > pivot:
            self.quickSelect(sets, pivot + 1, end, k)
        else:
            self.quickSelect(sets, start, pivot - 1, k)
    
    def partition(self, sets, start, end):
        pivot = end

        i = start
        for j in range(start, pivot):
            # If the j smaller than the pivot, swap i and j
            if sets[j][0] < sets[pivot][0]:
                sets[i], sets[j] = sets[j], sets[i]
                i += 1
        
        sets[i], sets[pivot] = sets[pivot], sets[i]
        return i 
