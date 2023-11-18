"""
Reverse linkedlist bisected (reverse first half and reverse last half)
input: 0 -> 1 -> 2 -> 3 -> 4 -> 5
output: 2 -> 1 -> 0 -> 5 -> 4 -> 3

input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
output: 2 -> 1 -> 0 -> 3 -> 6 -> 5 -> 4

"""
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def invertedBisection(head):
    if not head or not head.next:
        return head
    # Find the mid point and the length
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    new_head = reverseLL(head, slow)
    if not fast:
        head.next = reverseLL(slow, None)
    else:
        head.next = slow
        slow.next = reverseLL(slow.next, None)
    return new_head

def reverseLL(head, target):
    prev = None
    curr = head
    while curr and curr != target:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    print(prev and prev.value)
    return prev
