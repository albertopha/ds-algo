"""
[4,5,0,-2,-3,1], k = 5
 ^
 
 4 
 
[4,9,9,7,4,5]
 ^
[5,1-4,-4,-2,1]
 ^
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        sums = 0
        count = 0
        remainder_counts = [0] * k
        remainder_counts[0] = 1
        
        for i, val in enumerate(nums):
            sums += val
            remainder = (sums + k if sums < 0 else sums) % k
            count += remainder_counts[remainder]
            remainder_counts[remainder] += 1
        return count
