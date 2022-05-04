"""
s = 1
e = 
[2,6,4,8,10,9,15]
              ^


[2,4,4,8,9,9,15]
             ^

{
  6: 1,
  4: 1,
  8: 1,
  10: 1,
  9: 1,
  15: 1
}

s = 1
e = 3
ms = 5
[1,3,5,2,4]
     ^
 
[1,2,2,2,4]
     ^
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s, e = sys.maxsize, 0
        i1 = i2 = 0
        min_nums = self.getMinNums(nums)
        
        while i1 < len(nums):
            if nums[i1] <= min_nums[i2]:
                i1 += 1
                i2 += 1
                continue
            
            s = min(s, i1)
            max_seen = nums[i1]
            while i1 < len(nums) and i2 < len(nums) and max_seen > min_nums[i2]:
                max_seen = max(max_seen, nums[i1])
                e = max(e, i2)
                i1 += 1
                i2 += 1
            
            i1 = i2
        return e - s + 1 if s <= e else 0
    
    def getMinNums(self, nums: List[int]) -> List[int]:
        m = nums[-1]
        min_nums = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            m = min(m, nums[i])
            min_nums[i] = m
        return min_nums
