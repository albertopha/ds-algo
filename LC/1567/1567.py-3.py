"""
[1,-2,-3,4]
 ^
         ^
    
pos: 4
is_neg: False
max_len = 4



[-1,-2,-3,0,1]
          ^
  ^
pos: 0
is_neg: False
max_len = 2

[-1,1,2,3,4,5]
  ^
  ^

pos: 0
is_neg: False
max_len = 2

[0,1,-2,-3,-4]
 ^
 ^
 
pos: 3
is_neg: True
max_len = 3
"""
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l = 0
        is_neg = False
        max_len = 0
        for r in range(len(nums)):
            is_neg = not is_neg if nums[r] < 0 else is_neg
            
            while l <= r and nums[r] == 0:
                if not is_neg:
                    max_len = max(max_len, r-l)
                    
                is_neg = not is_neg if nums[l] < 0 else is_neg
                l += 1
            
            if not is_neg:
                max_len = max(max_len, r-l+1)
        
        while l < len(nums):
            if not is_neg:
                max_len = max(max_len, len(nums)-l)
            is_neg = not is_neg if nums[l] < 0 else is_neg
            l += 1
            
        return max_len
