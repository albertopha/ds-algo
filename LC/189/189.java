class Solution {
    public void rotate(int[] nums, int k) {
        if (nums.length == 0) return;
        
        int steps = k % nums.length;
        if (steps == 0) return;
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, steps-1);
        reverse(nums, steps, nums.length-1);
    }
    
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
