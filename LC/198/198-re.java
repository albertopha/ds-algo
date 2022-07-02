/*
[10,2,4,5]
[10,2,14,15]
*/
class Solution {
    public int rob(int[] nums) {
        int len = nums.length;
        
        for (int i = 2; i < len; i++) {
            int val1 = (i - 3 >= 0) ? nums[i-3] : 0;
            int val2 = nums[i-2];
            nums[i] += Math.max(val1, val2);
        }
        
        int val1 = (len >= 2) ? nums[len-2] : 0;
        int val2 = (len >= 1) ? nums[len-1] : 0;
        return Math.max(val1, val2);
    }
}
