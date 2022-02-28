import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root, int lo, int hi) {
        if (root == null) return 0;
        int count = 0;

        if (root.val >= lo && root.val <= hi) count++;
        if (root.val < lo) {
            count += solve(root.right, lo, hi);
        } else if (root.val > hi) {
            count += solve(root.left, lo, hi);
        } else {
            count += (solve(root.left, lo, hi) + solve(root.right, lo, hi));
        }
        return count;
    }
}