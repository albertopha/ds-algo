class Solution:
    def solve(self, nums):
        if not nums:
            return 0
        
        max_heights = [0] * len(nums)
        right_max_height = nums[-1]
        for i in range(len(nums)-1,-1,-1):
            right_max_height = max(right_max_height, nums[i])
            max_heights[i] = max(right_max_height, nums[i])
        
        area = 0
        left_max_height = nums[0]
        for i in range(1, len(nums)):
            left_max_height = max(left_max_height, nums[i])
            area += (min(left_max_height, max_heights[i]) - nums[i])
        return area
        
