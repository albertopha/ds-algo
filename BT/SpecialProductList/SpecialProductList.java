import java.util.*;

class Solution {
    public int[] solve(int[] nums) {
       if (nums.length == 0) return nums;

       int[] output = Arrays.copyOfRange(nums, 0, nums.length);
       for (int i = nums.length-2; i >= 0; i--) {
           output[i] = output[i] * output[i+1];
       }

       int leftProduct = 1;
       for (int i = 0; i < nums.length; i++) {
           if (i == 0) output[i] = output[i+1];
           else if (i == nums.length-1) output[i] = leftProduct;
           else output[i] = leftProduct * output[i+1];
           leftProduct *= nums[i];
       }
       return output;
    }
}
