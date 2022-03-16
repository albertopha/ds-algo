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
        int[] longest = new int[1];
        solve(root, longest);
        return longest[0];
    }

    public int solve(Tree root, int[] longest) {
        if (root == null) return 0;
        int leftHeight = 1 + solve(root.left, longest);
        int rightHeight = 1 + solve(root.right, longest);
        longest[0] = Math.max(longest[0], leftHeight + rightHeight - 1);
        return Math.max(leftHeight, rightHeight);
    }
}
