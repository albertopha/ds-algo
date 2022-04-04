import java.util.*;

class Solution {
    public int solve(int[] nums, int k) {
        if (nums.length == 0 || nums.length < k) return -1;
        return quickSelect(nums, 0, nums.length-1, k);
    }

    private int quickSelect(int[] nums, int start, int end, int k) {
        if (start >= end) return nums[start];
        int p = partition(nums, start, end);
        if (p == k) return nums[p];
        if (p < k) return quickSelect(nums, p+1, end, k);
        return quickSelect(nums, start, p-1, k);
    }

    private int partition(int[] nums, int start, int end) {
        int pivot = end;
        int s = start;
        for (int i = start; i < pivot; i++) {
            if (nums[i] < nums[pivot]) {
                swap(nums, s, i);
                s++;
            }
        }
        swap(nums, s, pivot);
        return s;
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
