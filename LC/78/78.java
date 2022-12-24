/*
                     [1, 2, 3]
                  /       |         \
         [1]             [2]         [3]
        /   \
    [1,2]   [1,3]
*/
class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> collections = new ArrayList<>();
        if (nums.length == 0) return collections; 
        collections.add(new ArrayList<Integer>());
        subsets(nums, 0, new ArrayList<Integer>(), collections);
        return collections;
    }

    private void subsets(int[] nums, int index, List<Integer> collection, List<List<Integer>> collections) {
        if (index == nums.length) return;
        for (int i = index; i < nums.length; i++) {
            int num = nums[i];
            collection.add(num);
            collections.add(new ArrayList<Integer>(collection));
            subsets(nums, i+1, collection, collections);
            collection.remove(collection.size() - 1);
        }
    }
}
