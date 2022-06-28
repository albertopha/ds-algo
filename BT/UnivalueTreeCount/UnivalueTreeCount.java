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
       int[] counts = new int[1];
       dfs(root, counts);
       return counts[0];
    }

    private boolean dfs(Tree node, int[] count) {
        if (node == null) return true;
        if (node.left == null && node.right == null) {
            count[0]++;
            return true;
        }
        
        boolean isLeftUnival = dfs(node.left, count);
        boolean isRightUnival = dfs(node.right, count);

        if (!isLeftUnival || !isRightUnival) return false;
        if (node.left != null && node.left.val != node.val) return false;
        if (node.right != null && node.right.val != node.val) return false;
        count[0]++;
        return true;
    }
}
