/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    if (nums.length === 0) return -1;
    
    let l = 0,
        r = nums.length-1;
    
    while (l <= r) {
        const m = Math.floor((l+r)/2);
        
        if (nums[m] == target) return m;
        if (nums[l] <= nums[m]) {
            if (nums[l] <= target && target < nums[m]) r = m-1;
            else l = m+1;
        } else {
            if (nums[m] < target && target <= nums[r]) l = m+1;
            else r = m-1;
        }
    }
    return -1;
};
