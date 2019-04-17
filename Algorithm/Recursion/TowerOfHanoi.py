#!
class TowerOfHanoi:
    def __init__(self):
        self.stack_start = []
        self.stack_middle = []
        self.stack_end = []
        return

    def migrate_hanoi(self, start):
        self.stack_start = start[:]
        self.stack_middle = []
        self.stack_end = []

        self.migrate_hanoi_rec(len(start), self.stack_start, self.stack_middle, self.stack_end)

        print(self.stack_start)
        print(self.stack_middle)
        print(self.stack_end)
        return self.validate(start)

    def migrate_hanoi_rec(self, n, s, m, e):
        if n <= 0:
            return

        self.migrate_hanoi_rec(n-1, s, e, m)
        top = s.pop()
        e.append(top)
        self.migrate_hanoi_rec(n-1, m, s, e)

    def validate(self, stack):
        if len(self.stack_start) + len(self.stack_middle) != 0:
            return False

        if len(self.stack_end) != len(stack):
            return False

        for i in range(len(self.stack_end)):
            if self.stack_end[i] != stack[i]:
                return False

        return True


if __name__ == '__main__':
    toh = TowerOfHanoi()
    print(toh.migrate_hanoi([1, 2, 3, 4, 5]))
