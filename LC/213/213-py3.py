class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        include_zero_index = self.robRange(nums, 0, len(nums)-1)
        include_end_index = self.robRange(nums, 1, len(nums))
        return max(include_zero_index, include_end_index)
    
    def robRange(self, nums: List[int], start: int, end: int) -> int:
        if len(nums) < 2:
            return nums[0]
        
        prev, curr = 0, 0
        
        for i in range(start, end):
            p = prev 
            prev = curr
            curr = max(p+nums[i], curr)
        return curr
