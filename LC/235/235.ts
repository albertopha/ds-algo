/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    if (!root) return null;
    if (root == p || root == q) return root;
    if (p.val <= root.val && q.val >= root.val) return root;
    if (p.val >= root.val && q.val <= root.val) return root;
    return (p.val < root.val)
        ? lowestCommonAncestor(root.left, p, q)
        : lowestCommonAncestor(root.right, p, q);
};
