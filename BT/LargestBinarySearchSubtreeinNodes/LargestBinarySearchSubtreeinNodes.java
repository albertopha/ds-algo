import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
 /*
 - # of nodes
 - is BST

    [1,3,2,5]
    [2,3,5,1]
 */
class Solution {
    Pair<Integer, Tree> largestTree = new Pair<>(0, null);

    public Tree solve(Tree root) {
        if (root == null) return root;
        dfs(root);
        return largestTree.getValue();
    }
    
    // Each recursion returns int[3]
    // int[0] = node counts
    // int[1] = maximum node value seen so far
    // int[2] = minimum node value seen so far
    private int[] dfs(Tree node) {
        if (node == null) return new int[]{0, Integer.MIN_VALUE, Integer.MAX_VALUE};

        int[] leftTree = dfs(node.left);
        int[] rightTree = dfs(node.right);

        // Invalid binary search tree
        if (leftTree[1] >= node.val || rightTree[2] <= node.val) {
            return new int[]{0, Integer.MIN_VALUE, Integer.MAX_VALUE};
        }

        int leftTreeCount = leftTree[0];
        int rightTreeCount = rightTree[0];
        int currCount = leftTreeCount + rightTreeCount + 1;

        if (this.largestTree.getKey() < currCount) {
            this.largestTree = new Pair<Integer, Tree>(currCount + 1, node);
        }

        return new int[]{
            currCount,
            Math.max(node.val, Math.max(leftTree[1], rightTree[1])),
            Math.min(node.val, Math.min(leftTree[2], rightTree[2]))
        };
    }
}
