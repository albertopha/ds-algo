import java.util.*;
/*
[1,1,1,0,0,1,0]
 ^
             ^

zeros = 2
*/

class Solution {
    public int solve(int[] nums, int k) {
        if (nums.length == 0) return 0;

        int l = 0,
            r = 0;
        int longest = 0;
        int zeros = 0;

        while (r < nums.length) {
            if (nums[r] == 0) zeros++;
            while (zeros > k && l <= r) {
                if (nums[l++] == 0) zeros--;
            }
            longest = Math.max(longest, (r - l + 1));
            r++;
        } 
        
        return longest;
    }
}
