/*
[-1,0,1,2,-1,-4]
[-4,-1,-1,0,1,2]
     ^
              ^
    
*/
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> output = new ArrayList<>();
        if (nums.length < 3) return output; 
        Arrays.sort(nums);
        for (int i = 0; i < nums.length-2 && nums[i] <= 0; i++) {
            int target = nums[i];
            if (i > 0 && nums[i-1] == nums[i]) continue;
            twoSum(nums, i+1, -nums[i], output);
        }
        return output;
    }
    
    private void twoSum(int[] nums, int start, int target, List<List<Integer>> output) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = start; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                List<Integer> current = new ArrayList<>();
                current.add(-target);
                current.add(map.get(nums[i]));
                current.add(nums[i]);
                output.add(current);
                while (i+1 < nums.length && nums[i] == nums[i+1]) i++;
            }
            map.put(target-nums[i], nums[i]);
        }
    }
}
