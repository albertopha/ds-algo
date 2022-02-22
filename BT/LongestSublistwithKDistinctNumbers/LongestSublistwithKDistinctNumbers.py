class Solution:
    def solve(self, k, nums):
        if not nums:
           return 0

        longest = 0
        distinct_count = 0
        counter = dict()
        for num in nums:
            counter[num] = 0

        l = 0
        for r, num in enumerate(nums):
            if counter[num] == 0:
                distinct_count += 1
            counter[num] += 1

            while l <= r and distinct_count > k:
                lnum = nums[l]
                counter[lnum] -= 1
                if counter[lnum] == 0:
                    distinct_count -= 1
                l += 1

            longest = max(longest, (r - l + 1))
        return longest 
