/**
[-1,0,1,2,-1,-4]
[-4,-1,-1,0,1,2]
*/
function threeSum(nums: number[]): number[][] {
    const output = [];
    if (nums.length === 0) return output; 
    nums.sort((a,b) => a-b);
    for (let i = 0 ; i < nums.length-2; i++) {
        if (i > 0 && nums[i-1] === nums[i]) continue;
        twoSum(nums, i+1, -nums[i], output);
    }
    return output;
};

function twoSum(nums: number[], index: number, target: number, output: number[][]): void {
    const map = new Map(); 
    for (let i = index; i < nums.length; i++) {
        if (map.has(nums[i])) {
            output.push([-target, map.get(nums[i]), nums[i]]);
            while (i+1 < nums.length && nums[i] === nums[i+1]) i++;
        }
        map.set(target-nums[i], nums[i]);
    }
};
