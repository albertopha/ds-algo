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
/*
[3,9,20,15,7]
     ^

[9,3,15,20,7]
   ^
*/
class Solution {
    private int preorderIdx;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorderIdx = 0;
        if (preorder.length == 0 || preorder.length != inorder.length) return null;
        return buildTreeHelper(preorder, inorder);
    }
    
    private TreeNode buildTreeHelper(int[] preorder, int[] inorder) {
        if (this.preorderIdx >= preorder.length) return null;
        
        TreeNode node = new TreeNode(preorder[this.preorderIdx++]);
        int inorderIdx = findIndex(inorder, node.val);
        
        // Should never happen!
        if (inorderIdx == -1) {
            System.out.println("should never happen!");
            return node;
        }
        
        node.left = (inorderIdx > 0)
            ? buildTreeHelper(preorder, Arrays.copyOfRange(inorder, 0, inorderIdx))
            : null;
        node.right = (inorderIdx < inorder.length-1)
            ? buildTreeHelper(preorder, Arrays.copyOfRange(inorder, inorderIdx+1, inorder.length))
            : null;
        return node;
    }
    
    private int findIndex(int[] array, int target) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) return i;
        }
        return -1;
    } 
}
