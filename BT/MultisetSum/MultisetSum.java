import java.util.*;
/*
        1    2    3
     /    \
    1, 
*/

class Solution {
    public int solve(int[] nums, int k) {
        if (nums.length == 0) return 0;
        Arrays.sort(nums);
        return combinationSum(nums, 0, k);
    }

    private int combinationSum(int[] nums, int index, int k) {
        if (k <= 0) return (k == 0) ? 1 : 0;
        int count = 0;
        for (int i = index; i < nums.length; i++) {
            if (nums[i] > k) break;
            count += combinationSum(nums, i, k-nums[i]);
        }
        return count;
    }
}
