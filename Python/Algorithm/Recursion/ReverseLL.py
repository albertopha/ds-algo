"""
Test cases:

1 -> 2 -> 3 -> 4  should be: 4 -> 3 -> 2 -> 1
1 or empty LL = return itself

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
class ReverseLL(object):
    def __init__(self):
        return

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # return self.reverseLLIterative(head)
        return self.reverseLLRecursive(head, head)

    def reverseLLIterative(self, head):
        curr, new_head = head, head

        while curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = new_head
            new_head = next_node

        return new_head

    def reverseLLRecursive(self, new_head, new_curr):
        if not new_curr.next:
            return new_head

        next_node = new_curr.next
        new_curr.next = next_node.next
        next_node.next = new_head

        return self.reverseLLRecursive(next_node, new_curr)


    def printOutList(self, head):
        curr = head

        p = ''

        while curr:
            p += str(curr.val) + '->'
            curr = curr.next

        return p + 'NULL'


if __name__ == '__main__':
    head = ListNode(0)
    curr = head

    for i in range(1, 5):
        curr.next = ListNode(i)
        curr = curr.next

    reverse = ReverseLL()
    print(reverse.printOutList(head))
    head = reverse.reverseList(head)
    print(reverse.printOutList(head))
