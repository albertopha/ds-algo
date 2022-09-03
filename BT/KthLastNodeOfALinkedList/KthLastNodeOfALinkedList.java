import java.util.*;

/**
* 3 nodes, 2
*/
/**
 * class LLNode {
 *   int val;
 *   LLNode next;
 * }
 */
class Solution {
    public int solve(LLNode node, int k) {
        if (node == null || k < 0) return -1;
        int targetIndex = getLength(node) - k - 1;
        LLNode tmp = node;
        for (int i = 0; i < targetIndex; i++) tmp = tmp.next;
        return tmp.val;
    }

    private int getLength(LLNode node) {
        LLNode tmp = node;
        int len = 0;
        while (tmp != null) {
            len++;
            tmp = tmp.next;
        }
        return len;
    }
}
