/*
[1,5,4,2,9,9,9], k = 3
     ^
         ^
 
{
    5: 0,
    4: 1,
    2: 1
}

unique = 2
*/
class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        if (nums.length < k) return 0;
        
        int left = 0;
        long currSum = 0;
        long maxSum = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int right = 0; right < nums.length; right++) {
            if ((right - left) == k) {
                counter.put(nums[left], counter.get(nums[left]) - 1);
                if (counter.get(nums[left]) == 0) counter.remove(nums[left]);
                currSum -= nums[left];
                left++;
            }
            
            int currentCount = counter.getOrDefault(nums[right], 0);
            counter.put(nums[right], currentCount+1);
            currSum += nums[right];
            
            if (counter.size() == k) maxSum = Math.max(maxSum, currSum);
            
        }
        return maxSum;
    }
}
