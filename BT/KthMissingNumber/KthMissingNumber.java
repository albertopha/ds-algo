import java.util.*;

/*
 0 1 2 3
[5,6,8,9]
[0,1,3,4]

3
*/
class Solution {
    public int solve(int[] nums, int k) {
        if (nums.length == 0) return 0;

        int missingNumInNums =  (nums[nums.length-1] - nums[0]) - (nums.length - 1);
        if (missingNumInNums < k) return nums[nums.length-1] + (k - missingNumInNums) + 1;

        for (int i = 1; i < nums.length; i++) {
            int gap = nums[i] - nums[i-1] - 1;
            if (gap > k) return nums[i-1] + k + 1;
            k -= gap;
        }
        
        return nums[nums.length-1]+k+1;
    }
}
