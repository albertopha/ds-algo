/*
[2,3,1,1,4]
=> [true, true, true, true, true]
*/
class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return false;
        return optimal(nums);
    }
    
    // Greedy solution O(n)
    // Explanation can be found at:
    // https://www.youtube.com/watch?v=Yan0cv2cLy8&t=1s
    private boolean optimal(int[] nums) {
        int goal = nums.length-1;
        for (int i = nums.length-1; i >= 0; i--) {
            if (i + nums[i] >= goal) goal = i;
        }
        return goal == 0;
    }
    
    // DP solution O(n^2)
    private boolean subOptimal(int[] nums) {
        boolean[] dp = new boolean[nums.length];
        dp[nums.length-1] = true;
        
        for (int i = nums.length-2; i >= 0; i--) {
            int minIte = Math.min(i + nums[i] + 1, nums.length);
            for (int j = i; j < minIte; j++) {
                if (dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
}
