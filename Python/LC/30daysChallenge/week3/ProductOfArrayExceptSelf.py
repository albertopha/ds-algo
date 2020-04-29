from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = nums[:]
        from_right = nums[:]
        
        for i in range(1, len(from_left)):
            curr = from_left[i]
            prev = from_left[i-1]
            from_left[i] = curr * prev
            
        for i in range(len(from_right)-2, -1, -1):
            curr = from_right[i]
            prev = from_right[i+1]
            from_right[i] = curr * prev
        
        for i in range(len(nums)):
            left = from_left[i-1] if i > 0 else 1
            right = from_right[i+1] if i < len(nums)-1 else 1
            nums[i] = left * right
        
        return nums