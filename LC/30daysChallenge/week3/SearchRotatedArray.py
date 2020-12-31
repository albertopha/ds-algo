import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      if len(nums) == 0:
        return -1
      
      start = 0
      end = len(nums)-1
      
      while start < end:
        mid = math.floor((start+end)/2)
        
        if nums[mid] > nums[end]:
          start = mid+1
        else:
          end = mid
        
      min_ind = start
      
      if target < nums[min_ind]:
        return -1
      
      if target == nums[min_ind]:
        return min_ind
      
      start = min_ind if nums[min_ind] <= target <= nums[len(nums)-1] else 0
      end = min_ind-1 if min_ind > 0 and target > nums[len(nums)-1] else len(nums)-1
  
      while start <= end:
        mid = math.floor((start+end)/2)
        
        if nums[mid] > target:
          end = mid-1
        elif nums[mid] < target:
          start = mid+1
        else:
          return mid
      
      return -1
