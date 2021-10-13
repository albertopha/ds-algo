/*
[1,2,3] => [1,3,2]

[1,3,2] => [2,1,3]
 ^
     ^
[2,3,1] => [2,1,3]
   ^ ^

[3,2,1] =>

*/
class Solution {
    public void nextPermutation(int[] nums) {
        if (nums.length == 1) return;
        int start = findDecrementPoint(nums);
        
        if (start == -1) {
            reverse(nums, 0, nums.length-1);
            return;
        }
        
        int end = findSwapPoint(nums, start); 
        swap(nums, start, end);
        reverse(nums, start+1, nums.length-1);
    }
    
    private void swap(int[] nums, int idx1, int idx2) {
        int tmp = nums[idx1];
        nums[idx1] = nums[idx2];
        nums[idx2] = tmp;
    }
    
    private int findSwapPoint(int[] nums, int start) {
        int point = start + 1;
        for (int i = start+1; i < nums.length; i++) {
            if (nums[start] < nums[i] && nums[i] <= nums[point]) {
                point = i;
            }
        }
        return point;
    }
    
    private int findDecrementPoint(int[] nums) {
        int index = -1;
        for (int i = nums.length-2; i >= 0; i--) {
            if (nums[i] < nums[i+1]) {
                index = i;
                break;
            }
        }
        return index;
    }
    
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start++, end--);
        }
    }
}