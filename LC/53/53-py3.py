"""
[-2,1,-3,4,-1,2,1,-5,4]
         ^
         ^
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_sum, curr_sum = nums[0], 0 
        l = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            while l < r and nums[r] > curr_sum:
                curr_sum -= nums[l]
                l += 1
            
            max_sum = max(max_sum, curr_sum)
        return max_sum
