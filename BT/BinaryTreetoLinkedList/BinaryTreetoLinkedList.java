import java.util.*;

/**
 * public class Tree {
 *   int val;
 *   Tree left;
 *   Tree right;
 * }
 */

/**
 * class LLNode {
 *   int val;
 *   LLNode next;
 * }
 */
class Solution {
    public LLNode solve(Tree root) {
       if (root == null) return null; 

       LLNode head = new LLNode(-1);
       LLNode tmpLLNode = head;

       Tree tmpTreeNode = root;
       Stack<Tree> stack = new Stack<>();

       while (tmpTreeNode != null || !stack.isEmpty()) {
           while (tmpTreeNode != null) {
               stack.push(tmpTreeNode);
               tmpTreeNode = tmpTreeNode.left;
           }

           tmpTreeNode = stack.pop();
           tmpLLNode.next = new LLNode(tmpTreeNode.val);
           tmpLLNode = tmpLLNode.next;
           tmpTreeNode = tmpTreeNode.right;
       }

       return head.next;
    }
}
