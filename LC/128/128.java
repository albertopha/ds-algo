/*
(100,4,200,1,3,2,5)
Find the starting point.
*/
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        
        int longest = 0;
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) set.add(nums[i]);
        
        for (int num: nums) {
            if (set.contains(num-1)) continue;
            
            int currNum = num;
            int currCount = 0;
            
            while (set.contains(currNum++)) currCount++;
            longest = Math.max(longest, currCount);
        }
        return longest;
    }   
}
