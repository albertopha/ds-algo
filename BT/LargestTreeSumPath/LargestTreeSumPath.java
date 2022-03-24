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
        int[] maxSum = new int[]{root.val};
        dfs(root, maxSum);
        return maxSum[0];
    }

    private int dfs(Tree node, int[] maxSum) {
        if (node == null) return 0;

        int leftSum = Math.max(dfs(node.left, maxSum), 0);
        int rightSum = Math.max(dfs(node.right, maxSum), 0);
        maxSum[0] = Math.max(maxSum[0], leftSum + rightSum + node.val);
        return node.val + Math.max(leftSum, rightSum);
    }
}
