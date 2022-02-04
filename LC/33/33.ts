/*
[0,1,2,3,4]
first < mid < last (sorted)

[2,3,4,0,1]
first < mid (sorted)
last < mid

[3,4,0,1,2]
first > mid
mid < last (sorted)

*/
function search(nums: number[], target: number): number {
    if (!nums.length) return -1;
    let first = 0,
        last = nums.length-1;
    
    while (first <= last) {
        const mid = Math.floor((first+last)/2);
        
        if (nums[mid] === target) return mid;
        if (nums[first] < nums[last]) {
            if (target < nums[mid]) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        } else if (nums[first] <= nums[mid]) {
            if (target >= nums[first] && target < nums[mid]) {
                last = mid - 1;
            } else {
                first = mid + 1;
            }
        } else if (nums[mid] <= nums[last]) {
            if (target > nums[mid] && target <= nums[last]) {
                first = mid + 1;
            } else {
                last = mid - 1;
            }
        } else break;
    }
    return -1;
};
