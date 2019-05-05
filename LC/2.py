class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class AddTwoNumbers(object):
    @staticmethod
    def add_two_numbers_brute(l1, l2):
        prev, p1, p2 = l1, l1, l2
        curr = 0
        flag = 0

        if p1:
            curr += p1.val
            p1 = p1.next
        if p2:
            curr += p2.val
            p2 = p2.next

        if curr >= 10:
            curr %= 10
            flag = 1

        prev.val = curr

        while p1 or p2:
            curr = 0
            if p1:
                curr += p1.val
                p1 = p1.next
            if p2:
                curr += p2.val
                p2 = p2.next
            if flag:
                curr += 1
                flag = 0
            if curr >= 10:
                curr -= 10
                flag = 1
            if prev.next:
                prev.next.val = curr
            else:
                prev.next = ListNode(curr)
            prev = prev.next

        if flag:
            prev.next = ListNode(1)

        return l1


if __name__ == '__main__':
    atn = AddTwoNumbers()
    ln = ListNode(2)
    tn = ln
    tn.next = ListNode(4)
    tn = tn.next
    tn.next = ListNode(3)

    atn.add_two_numbers_brute(ln, ln)

    tn = ln
    while tn:
        print(tn.val)
        tn = tn.next
