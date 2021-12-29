class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set(nums)
        max_len = 1
        for num in nums:
            if num-1 not in seen:
                curr_val = num
                curr_len = 0
                
                while curr_val in seen:
                    curr_val += 1
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        return max_len
