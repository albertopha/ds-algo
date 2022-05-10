import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root) {
       if (root == null) return 0;
       int[] sums = new int[1];
       solve(root, 0, sums);
       return sums[0]; 
    }

    private void solve(Tree node, int sum, int[] sums) {
        if (node == null) {
            return;
        }

        if (node.left == null && node.right == null) {
            sums[0] += (sum*10+node.val);
        }
        solve(node.left, sum*10+node.val, sums);
        solve(node.right, sum*10+node.val, sums);
    }
}
