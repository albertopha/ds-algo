/*
[3,2,1,0,4]
         ^
 ^
 
 [3,0,0,1,4]
  ^
  ^
*/
class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) return false;
        
        int target = nums.length-1;
        for (int i = nums.length-1; i >= 0; i--) {
            if (i + nums[i] >= target) target = i;
        }
        return target == 0;
    }
}
