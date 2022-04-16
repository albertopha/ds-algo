/*
[2,3,-2,4]
        ^

min = -48
max = -8
result = 6

[2,3,-2,4,-3]
           ^

min = -12
max = 144
result = 144

*/
class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 0) return 0;
        boolean hasOverZero = false;
        int result = Arrays.stream(nums).max().getAsInt();
        int maxProduct = 1;
        int minProduct = 1;
        for (int i = 0 ; i < nums.length; i++) {
            int tmpMaxProduct = nums[i] * maxProduct;
            maxProduct = Math.max(tmpMaxProduct, Math.max(minProduct * nums[i], nums[i]));
            minProduct = Math.min(tmpMaxProduct, Math.min(minProduct * nums[i], nums[i]));
            result = Math.max(result, maxProduct);
        }
        
        return result;
    }
}
