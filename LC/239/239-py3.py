"""
[1,3,-1,-3,5,3,6,7], k = 3
     ^
           ^
 
pq = [5,-1,-3]
{
    -1: 1,
    -3: 1,
    5: 1
}

"""
import heapq
from collections import defaultdict

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        left = 0
        pq, output = [], []
        counter = defaultdict(lambda: 0)
        
        for right, num in enumerate(nums):
            if right < k-1:
                counter[num] += 1
                heapq.heappush(pq, -num)
                continue
            
            counter[num] += 1
            heapq.heappush(pq, -num)
            output.append(-pq[0])
            
            counter[nums[left]] -= 1
            if counter[nums[left]] <= 0:
                del counter[nums[left]]
            left += 1
            
            while pq and -pq[0] not in counter:
                heapq.heappop(pq)
        
        return output
        
        
