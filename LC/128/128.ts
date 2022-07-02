/*
[100,4,200,1,3,2]

{
    100,
    4,
    200,
    1,
    3,
    2
    
}

99
*/
function longestConsecutive(nums: number[]): number {
    if (nums.length === 0) return 0;
    
    const set = nums.reduce((s, num) => {
        s.add(num);
        return s;
    }, new Set());
    
    let len = 0;
    for (let i = 0; i < nums.length; i++) {
        if (set.has(nums[i]-1)) continue;
        let nextNums = nums[i];
        while (set.has(nextNums)) nextNums++;
        len = Math.max(len, nextNums-nums[i]);
    }
    return len;
};
