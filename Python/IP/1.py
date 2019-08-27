"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        if not l1 or not l2:
            return l1 if l1 else l2

        return self.brute_force(l1, l2)

    @staticmethod
    def brute_force(l1: ListNode, l2: ListNode) -> ListNode:
        new_node_head = None
        new_node_curr = new_node_head
        l1_curr = l1
        l2_curr = l2

        flag = 0
        while l1_curr or l2_curr or flag:
            count = flag
            if l1_curr:
                count += l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr:
                count += l2_curr.val
                l2_curr = l2_curr.next

            flag = count // 10
            count = count % 10

            if not new_node_head:
                new_node_head = ListNode(count)
                new_node_curr = new_node_head
            else:
                new_node_curr.next = ListNode(count)
                new_node_curr = new_node_curr.next

        return new_node_head

    @staticmethod
    def print(l: ListNode):
        count = ''
        curr = l

        if l:
            count = str(curr.val)
            curr = curr.next

        while curr:
            count += '-> ' + str(curr.val)
            curr = curr.next

        return count


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(3)
    l2.next = ListNode(9)
    l2.next.next = ListNode(6)
    l2.next.next.next = ListNode(9)
    l2.next.next.next.next = ListNode(7)

    result_list_node = s.addTwoNumbers(l1, l2)
    print(s.print(result_list_node))

    l3 = ListNode(2)
    l3.next = ListNode(4)
    l3.next.next = ListNode(3)

    l4 = ListNode(5)
    l4.next = ListNode(6)
    l4.next.next = ListNode(4)

    result_list_node2 = s.addTwoNumbers(l3, l4)
    print(s.print(result_list_node2))

