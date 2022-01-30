function maxSubArray(nums: number[]): number {
    if (nums.length == 0) return 0;
    
    let l = 0;
    let maxSum = nums[0],
        sum = nums[0];
    for (let r = 1; r < nums.length; r++) {
        sum += nums[r];
        while (l < r && nums[r] > sum) sum -= nums[l++];
        maxSum = Math.max(maxSum, sum);
    }
    return maxSum;
};
