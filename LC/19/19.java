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
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;
        int size = getSize(head);
        if (size == 1 && n == 1) return null;
        if (size == n) return head.next;
        removeNthNode(head, size-n);
        return head;
    }
    
    private int getSize(ListNode head) {
        ListNode tmp = head;
        int size = 0;
        while (tmp != null) {
            tmp = tmp.next;
            size++;
        }
        return size;
    }
    
    private void removeNthNode(ListNode head, int n) {
        ListNode tmp = head;
        ListNode tmpNext = tmp.next;
        
        for (int i = 1; i < n; i++) {
            tmp = tmp.next;
            tmpNext = tmpNext.next;
        }
        
        if (tmp != null) {
            tmp.next = (tmpNext != null) ? tmpNext.next : null;
        }
    }
}
