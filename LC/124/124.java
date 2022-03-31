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
    public int maxPathSum(TreeNode root) {
        if (root == null) return 0;
        int[] maxSum = new int[]{root.val};
        maxPathSum(root, maxSum);
        return maxSum[0];
    }
    
    private int maxPathSum(TreeNode node, int[] maxSum) {
        if (node == null) return 0;
        
        int leftSubtreeSum = maxPathSum(node.left, maxSum);
        int rightSubtreeSum = maxPathSum(node.right, maxSum);
        leftSubtreeSum = Math.max(leftSubtreeSum, 0);
        rightSubtreeSum = Math.max(rightSubtreeSum, 0);
                
        maxSum[0] = Math.max(maxSum[0], leftSubtreeSum + rightSubtreeSum + node.val);
        return node.val + Math.max(leftSubtreeSum, rightSubtreeSum);
    }
}
