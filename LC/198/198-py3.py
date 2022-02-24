"""
[2,7,9,3,1,5]
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        for i in range(2, len(nums)):
            if i - 3 >= 0:
                nums[i] += max(nums[i-2], nums[i-3])
            else:
                nums[i] += nums[i-2]
        return max(nums[-1], nums[-2])
