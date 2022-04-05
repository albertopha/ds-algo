"""
[10,9,2,5,3,7,101,18]

                ""
               /  \  ... \
             10    9     18
            /  \
          9    2...

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # return self.topDown(nums, 0, -sys.maxsize, [None for _ in range(len(nums))])
        return self.bottomUp(nums)
    
    def bottomUp(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
    
    def topDown(self, nums: List[int], index: int, prev: int, dp: List[int]) -> int:
        if index >= len(nums):
            return 0
        
        if dp[index] != None:
            return dp[index]
        
        longest = 0
        for i in range(index, len(nums)):
            if prev >= nums[i]:
                continue
            
            longest = max(longest, 1 + self.topDown(nums, i+1, nums[i], dp))
        dp[index] = longest
        return longest
        
