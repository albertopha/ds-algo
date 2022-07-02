/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

/*
----------------------------
[Ex 1]

L0 -> L1 -> L2
      ^
             ^

[L1, L2]

L0 -> L2 -> L1
----------------------------
[Ex 2]
L0 -> L1 -> L2 -> L3
             ^
                      ^

stack = [L2, L3]
L0 -> L3 -> L1 -> L2

----------------------------
[Ex 3]

L0 -> L1 -> L2 -> L3 -> L4
            ^
                         ^

[L2, L3, L4]
L0 -> L4 -> L1 -> L3 -> L2
----------------------------
*/
class Solution {
    public void reorderList(ListNode head) {
        if (head == null) return;
        
        ListNode slow = head; 
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        Stack<ListNode> stack = new Stack<>();
        while (slow != null) {
            ListNode nextNode = slow.next; 
            slow.next = null;
            stack.push(slow);
            slow = nextNode;
        }
        
        ListNode node = head;
        while (node != null) {
            ListNode nextNode = node.next;
            ListNode stackNode = (!stack.isEmpty()) ? stack.pop() : null;
            node.next = stackNode;
            if (stackNode != null) stackNode.next = nextNode;
            node = (nextNode != null) ? nextNode : stackNode;
        }
    }
}
