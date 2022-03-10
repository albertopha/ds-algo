class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums[0] if nums else 0
        
        output = nums[:]
        for i in range(len(nums)-2, -1, -1):
            output[i] *= output[i+1]
        
        curr = 1
        for i in range(len(nums)):
            if i == 0:
                output[0] = output[1]
            elif i == len(nums)-1:
                output[-1] = curr
            else:
                output[i] = curr * output[i+1]
            curr *= nums[i]
        return output
