import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public boolean solve(Tree root0, Tree root1) {
        return compareTrees(root0, root1);
    }

    private boolean compareTrees(Tree node0, Tree node1) {
        if (node0 == null || node1 == null) return node0 == node1;
        if (node0.val != node1.val) return false;
        if (
            !(
                compareTrees(node0.left, node1.left) &&
                compareTrees(node0.right, node1.right)
            )
        ) return false;
        return true;
    }
}
