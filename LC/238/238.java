/*
================================================================
Test cases:
#1
[1,2,3,4]
allProduct = 24
[24/1, 24/2, 24/3, 24/4]
-> [24, 12, 8, 6]

#2
[1, 2]
-> [2, 1]
================================================================
Brute force:
1. Iterate from i = 0 to i = nums.length:
    a. define variable, currProduct = 1;
    b. Iterate from j = 0 to j = nums.length:
        a. if j != i, currProduct *= nums[j]
        b. insert into the ArrayList<Integer>.
        
Time: O(N^2)
Space: O(N)
================================================================
(Sub-optimal) Solution with division:
1. product of all num in nums list (int allProduct).
2. for i = 0 to nums.length:
    num[i] = allProduct / num[i]
    
Time: O(N)
Space: O(1)
===============================================================
(Sub-optimal) Without division:
lefts = [1, 1*2, 1*2*3, 1*2*3*4]
rights = [1*2*3*4, 2*3*4, 3*4, 4]

1. Two arrays, lefts and rights, which are the products from left to right
    and from right to left, respectively.
2. Iterate through nums from i = 0 to i = nums.length:
    a. if i == 0, nums[i] = rights[i+1]
    b. nums[i] = lefts[i-1] * rights[i+1]
    c. if i == nums.length - 1, nums[i] = lefts[i-1]

Time: O(N)
Space: O(N)
================================================================
(Optimal) Constant space:
[1,2,3,4]
rights = [1*2*3*4, 2*3*4, 3*4, 4]

1. Make output array as the rights array.
2. Traverse from left to right while keeping the products.

Time: O(N)
Space: O(1)
================================================================
*/
class Solution {
    public int[] productExceptSelf(int[] nums) {
        if (nums == null || nums.length < 2) {
            return nums;
        }
        
        return productExceptSelfConstantSpace(nums);
    }
    
    private int[] productExceptSelfConstantSpace(int[] nums) {
        int[] output = generateProducts(nums, 1);
        int lefts = 1;
        
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) output[i] = output[i + 1];
            else if (i == nums.length - 1) output[i] = lefts;
            else output[i] = output[i + 1] * lefts;
            lefts *= nums[i];
        }
        
        return output;
    }
    
    private int[] productExceptselfTwoArrays(int[] nums) {
        int[] lefts = generateProducts(nums, 0);
        int[] rights = generateProducts(nums, 1);
        
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                nums[i] = rights[i + 1];
            } else if (i == nums.length - 1) {
                nums[i] = lefts[i - 1];
            } else {
                nums[i] = lefts[i - 1] * rights[i + 1];
            }
        }
        
        return nums;
    }
    
    private int[] generateProducts(int[] nums, int direction) {
        int size = nums.length;
        int[] arr = new int[size];
        if (direction == 0) {
            arr[0] = nums[0];
            for (int i = 1; i < size; i++) {
                arr[i] = nums[i] * arr[i - 1];
            }
        } else {
            arr[size-1] = nums[size-1];
            for (int i = size-2; i >= 0; i--) {
                arr[i] = nums[i] * arr[i + 1];
            }
        }
        
        return arr;
    }
}
