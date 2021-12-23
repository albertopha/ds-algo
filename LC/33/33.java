/*
[1,2,3,4,5,6,7]

[2,3,4,5,6,7,1]
target = 3
    => l = 2, r = 1, m = 5
    => l <= target < m
    
target = 7
    => 

[4,5,6,7,1,2,3]

Tip: see which side (ie. upper or bottom half) is sorted.
*/
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length == 0) return -1;
        
        int left = 0,
            right = nums.length-1;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            
            if (nums[mid] == target) return mid;
            
            // Upper half is sorted
            if (nums[mid] < nums[right]) {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else { // Bottom half is sorted
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        
        return -1;
    }
}
