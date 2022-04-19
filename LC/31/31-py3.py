"""
[1,2,3] => [1,3,2]

[1,3,2] => [2,1,3]
 ^
     ^
     => [2,3,1]
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        drop = self.findDropPoint(nums)
        
        if drop == -1:
            nums.reverse()
            return
        
        swap = self.findSwapPoint(nums, drop)
        nums[drop], nums[swap] = nums[swap], nums[drop]
        
        self.reverse(nums, drop, len(nums)-1)
        
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        i = start+1
        while i < end:
            nums[i], nums[end] = nums[end], nums[i]
            i+=1
            end-=1
        
    def findSwapPoint(self, nums: List[int], start: int) -> int:
        swap = start+1
        for i in range(start, len(nums)):
            if nums[start] < nums[i] <= nums[swap]:
                swap = i
        return swap
        
    def findDropPoint(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            prev, curr = nums[i-1], nums[i]
            if prev < curr:
                return i-1
        return -1
