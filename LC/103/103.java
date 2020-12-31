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
=============================================
Test case:
#1
[]
[[]]

#2
[3,9,20,null,null,15,7]
[
    [3],
    [20, 9],
    [15, 7]
]
=============================================
Brute force:
1. Perform BFS level by level
    with flag indicating whether the
    node should be added from left to right or
    right to left.
    
    ie. fromRight? -> add from right to left
    
Time: O(N), N = #of nodes
Space: O(N), queue size
=============================================
Optimal:
=============================================
*/
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        if (root == null) {
            return result;
        }
        
        boolean fromRight = false;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> current = new ArrayList<>();
            
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                
                // Add from right to left
                if (fromRight) {
                    current.add(0, node.val);
                } else { // add from left to right
                    current.add(node.val);
                }
                
                if (node.left != null) {
                    queue.offer(node.left);
                }
                
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.add(current);
            fromRight = !fromRight;
        }
        
        return result;
    }
} 
