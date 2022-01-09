import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root, int t) {
        int inorderSuccessor = Integer.MAX_VALUE;
        if (root == null) return inorderSuccessor;

        while (root != null) {
            if (root.val > t) {
                inorderSuccessor = Math.min(inorderSuccessor, root.val);
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return inorderSuccessor;
    }

    // public int solve(Tree root, int t) {
    //     if (root == null) return -1;

    //     Tree node = root;
    //     int inorderSuccessor = Integer.MAX_VALUE;

    //     // Search the target node
    //     while (node != null) {
    //         if (node.val == t) break;
    //         if (node.val < t) node = node.right;
    //         else {
    //             if (node.val > t && inorderSuccessor > node.val) inorderSuccessor = node.val;
    //             node = node.left;
    //         }
    //     }

    //     if (node.right != null) {
    //         node = node.right;
    //         while (node != null) {
    //             if (inorderSuccessor > node.val) inorderSuccessor = node.val;
    //             node = node.left;
    //         }
    //     };
    //     return inorderSuccessor;
    // }
}
