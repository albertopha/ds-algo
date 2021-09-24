from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        
        counter = Counter(nums)
        elements = []
        
        for num, count in counter.items():
            if not elements:
                elements.append((count, num))
                continue
                
            if len(elements) == k:
                if elements[0][0] >= count:
                    continue
                heapq.heappop(elements)
            
            heapq.heappush(elements, (count, num))
        
        return list(map(lambda x: x[1], elements))
        