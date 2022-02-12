import java.util.*;

class Solution {
    public int solve(int[] nums) {
        if (nums.length == 0) return 0;

        int[] maxHeightRightToLeft = new int[nums.length];
        int maxHeight = nums[nums.length-1];

        for (int i = nums.length-1; i >= 0; i--) {
            maxHeight = Math.max(maxHeight, nums[i]);
            maxHeightRightToLeft[i] = maxHeight;
        }

        int sum = 0;
        int maxHeightLeftToRight = nums[0];

        for (int i = 0; i < nums.length; i++) {
            maxHeightLeftToRight = Math.max(nums[i], maxHeightLeftToRight);
            sum += Math.min(maxHeightLeftToRight, maxHeightRightToLeft[i]) - nums[i];
        }

        return sum;
    }
}
