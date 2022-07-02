/**
 * class Tree {
 *     val: number;
 *     left: Tree | null;
 *     right: Tree | null;
 * 
 *     constructor(val: number, left: Tree | null, right: Tree | null) {
 *         this.val = val
 *         this.left = left
 *         this.right = right
 *     }
 * }
 */
class Solution {
    solve(root: Tree, t: number): number {
       if (!root) return -1;

       let node = root;
       let output = t;
       while (node) {
           if (node.val > t) {
               output = node.val;
               node = node.left;
           } else {
               node = node.right;
           }
       }
       return output;
    }
}
