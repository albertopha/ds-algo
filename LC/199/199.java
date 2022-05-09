/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> output = new ArrayList<>();
        if (root == null) return output; 
        
        List<TreeNode> deque = new LinkedList<>();
        deque.add(root);
        
        while (!deque.isEmpty()) {
            int size = deque.size();
            output.add(deque.get(deque.size()-1).val);
            for (int i = 0; i < size; i++) {
                TreeNode node = deque.remove(0);
                if (node.left != null) deque.add(node.left);
                if (node.right != null) deque.add(node.right);
            }
        }
        
        return output;
    }
}
