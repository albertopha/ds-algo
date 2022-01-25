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

function isValidBST(root: TreeNode | null): boolean {
    if (!root) return false;
    const traversals = [];
    inorderTraversal(root, traversals);
    return traversals.every((node, i) => i === 0 || traversals[i-1] < node);
};

function inorderTraversal(node: TreeNode, traversals: number[]): void {
    if (!node) return;
    inorderTraversal(node.left, traversals);
    traversals.push(node.val);
    inorderTraversal(node.right, traversals);
};
