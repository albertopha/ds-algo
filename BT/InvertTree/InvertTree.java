import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public Tree solve(Tree root) {
        if (root == null) return null;
        Tree left = solve(root.left);
        Tree right = solve(root.right);
        Tree invertedRoot = new Tree(root.val);
        invertedRoot.left = right;
        invertedRoot.right = left;
        return invertedRoot;
    }
}
