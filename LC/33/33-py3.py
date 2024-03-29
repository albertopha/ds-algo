"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

low < mid ->
    if low < target < mid -> lower half else upper half
low > mid ->
else return -1
[4,5,6,7,0,1,2], target = 0
       ^
       
[3,1], target = 1
 ^

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid -1
        return -1
