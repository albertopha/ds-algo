// ! Re - py -> remove duplicate

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Forty {
	public List<List<Integer>> combinationSum2(int[] candidates, int target) {
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		Arrays.sort(candidates);
        bruteForce(candidates, target, new ArrayList<Integer>(), result, 0);
        return result;
    }
	
	private void bruteForce(int[] candidates, int target, List<Integer> curr, List<List<Integer>> list, int start) {
		
		if (target == 0) {
			list.add(new ArrayList<Integer>(curr));
			return;
		}
		
		if (target < 0) {
			return;
		}
		
		for (int i = start; i < candidates.length; i++) {
			int sum = target - candidates[i];
			if (sum < 0 || (i > start && candidates[i] == candidates[i-1])) continue;

			curr.add(candidates[i]);
			bruteForce(candidates, sum, curr, list, i+1);
			curr.remove(curr.size()-1);
		}
	}
	
	public static void main(String[] args) {
		Forty forty = new Forty();
		int[] candidates1 = {10, 1, 2, 7, 6, 1, 5};
		
		List<List<Integer>> result1 = forty.combinationSum2(candidates1, 8);
		System.out.println(result1);
	}
}
