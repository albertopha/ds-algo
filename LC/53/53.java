class Solution {
    public int maxSubArray(int[] nums) {
        if (nums == null) {
            return 0;
        }
        
        int start = 0;
        int sum = 0;
        int maxInt = Integer.MIN_VALUE;
        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];
            while (sum < nums[end]) {
                sum -= nums[start];
                start++;
            }
            maxInt = Math.max(maxInt, sum);
        }
        
        return maxInt;
    }
}
