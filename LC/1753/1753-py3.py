"""
a = 2, b = 4 , c = 6
(2,3,5)
(2,2,4)
(1,2,3)
(1,1,2)
(0,1,1)
(0,0,0)
"""
import heapq
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return self.optimal(a,b,c)
    
    def optimal(self, a: int, b: int, c: int) -> int:
        piles = sorted([a,b,c])
        
        if piles[0] + piles[1] <= piles[2]:
            return piles[0] + piles[1]
        
        return sum(piles) // 2
        
    def bruteForce(self, a: int, b: int, c: int) -> int:
        count = 0
        piles = [-a, -b, -c]
        heapq.heapify([-a, -b, -c])
        
        while len(piles) > 1:
            highest = -heapq.heappop(piles) - 1
            second_highest = -heapq.heappop(piles) - 1
            
            if highest > 0:
                heapq.heappush(piles, -highest)
            
            if second_highest > 0:
                heapq.heappush(piles, -second_highest)
            
            count += 1 
        
        return count
