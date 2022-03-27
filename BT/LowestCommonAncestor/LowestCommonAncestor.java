import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int solve(Tree root, int a, int b) {
        if (root == null) return -1;
        Set<Integer> paths = new HashSet<>();
      
        dfs(root, a, paths);
        paths.add(a);
      
        if (paths.contains(b)) return b;
      
        int[] ancestor = new int[]{b};
        findLowestCommonAncestor(root, b, ancestor, paths);
        return ancestor[0];
    }

    private boolean findLowestCommonAncestor(Tree node, int target, int[] ancestor, Set<Integer> paths) {
        if (node == null) return false;
        if (node.val == target) return true;

        boolean findLeft = findLowestCommonAncestor(node.left, target, ancestor, paths);
        boolean findRight = findLowestCommonAncestor(node.right, target, ancestor, paths);
        if (findLeft || findRight) {
            if (paths.contains(node.val) && ancestor[0] == target) {
                ancestor[0] = node.val;
            }
            return true;
        }
        return false;
    }

    private boolean dfs(Tree node, int target, Set<Integer> paths) {
        if (node == null) return false;
        if (node.val == target) return true;

        boolean findLeft = dfs(node.left, target, paths);
        boolean findRight = dfs(node.right, target, paths);
        if (findLeft || findRight) {
            paths.add(node.val);
            return true;
        }
        return false;
    }
}
