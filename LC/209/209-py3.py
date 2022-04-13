class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return -1
        
        sums, l, count = 0, 0, sys.maxsize
        for r in range(len(nums)):
            sums += nums[r]
            
            while l <= r and sums >= target:
                count = min(count, r-l+1)
                sums -= nums[l]
                l+=1
            
        return count if count < sys.maxsize else 0
