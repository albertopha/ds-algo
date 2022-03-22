from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        counter = Counter(nums)
        frequency = []
        
        for val, counts in counter.items():
            heapq.heappush(frequency, (-counts, val))
        
        frequent = []
        for i in range(k):
            frequent.append(heapq.heappop(frequency)[1])
        return frequent
        
