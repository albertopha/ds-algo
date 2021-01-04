/*
============================================
Test cases:
[1,2,3,1]
       ^

amount = 1 + 3 = 4
maxAmount = 1 + 3 = 4

amount = 2 + 1 = 3
maxAmount = 2 + 1 = 3

[2,7,9,3,1]
         ^
dp = [2,7,11,11,12]
dp[i] = max(dp[i] + dp[i-2], dp[i-1])

============================================
Brute force:
1. Recursion:
    two choices -->
        a. rob the current house:
            skip the next house
        b. skip the current house:
            move to the next house
2. Compute the maxAmount resulted from the recursion.

Time: O(2^N) two choices
Space: O(N) recursion stack
============================================
Optimal:
1. dynamic programming with the following equation:
dp[i] = max(nums[i] + dp[i-2], dp[i-1])
===========================================
*/
class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        if (nums.length == 1) {
            return nums[0];
        }
        
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(nums[i] + dp[i-2], dp[i-1]);
        }
        
        return dp[dp.length - 1];
    }
}
