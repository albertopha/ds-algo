class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        goal = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
