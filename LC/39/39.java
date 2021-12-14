/*
            [2,3,6,7], i = 0, t = 7
            /
        [2], 0, 5
        /
      [2,2], 0, 3
      /             \
    [2,2,2], 0, 1    [2,2,3], 1, 0
    /       
   X        
*/
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList<>();
        if (candidates.length == 0) return results;
        combinationSum(candidates, 0, target, new ArrayList<Integer>(), results);
        return results;
    }
    
    private void combinationSum(int[] candidates, int index, int target, List<Integer> current, List<List<Integer>> results) {
        if (target == 0) {
            results.add(new ArrayList(current));
            return;
        }
        
        for (int i = index; i < candidates.length; i++) {
            if (candidates[i] > target) continue;
            current.add(candidates[i]);
            combinationSum(candidates, i, target-candidates[i], current, results);
            current.remove(current.size()-1);
        }
    }
}
