class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_val = nums[0]
        
        while l <= r:
            m = (l + r) // 2
            min_val = min(min_val, nums[m])
            
            if nums[m] <= nums[r]:
                r = m-1
            else:
                l = m+1
        return min_val
            
        
