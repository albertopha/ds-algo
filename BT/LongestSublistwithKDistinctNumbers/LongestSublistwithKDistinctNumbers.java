/*
Problem: https://binarysearch.com/problems/Longest-Sublist-with-K-Distinct-Numbers

k = 2
[0, 1, 2, 1, 0]
    ^
             ^

unique = 3
seen = (0, 1, 2)
*/
import java.util.*;

class Solution {
    public int solve(int k, int[] nums) {
        if (nums.length == 0 || k == 0) return 0;

        int maxLength = 1;
        int uniqueCounter = 0;
        Map<Integer, Integer> counter = new HashMap<>();

        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            if (!counter.containsKey(nums[right])) {
                counter.put(nums[right], 0);
                uniqueCounter++;
            }
            counter.put(nums[right], counter.get(nums[right]) + 1);

            while (uniqueCounter > k) {
                counter.put(nums[left], counter.get(nums[left]) - 1);
                if (counter.get(nums[left]) == 0) {
                    counter.remove(nums[left]);
                    uniqueCounter--;
                }
                left++;
            }

            maxLength = Math.max(maxLength, (right - left + 1));
        }

        return Math.max(maxLength, (nums.length - left));
    }
}
