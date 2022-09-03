import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */
class Solution {
    public int[] solve(Tree root) {
        if (root == null) return new int[0];

        Tree node = root;
        Stack<Tree> stack = new Stack<>();
        List<Integer> traversal = new ArrayList<>();
        
        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                stack.add(node);
                node = node.left;
            }

            node = stack.pop();
            traversal.add(node.val);
            node = node.right;
        }

        int[] result = new int[traversal.size()];
        for (int i = 0; i < traversal.size(); i++)
            result[i] = traversal.get(i);
        return result;
    }
}
