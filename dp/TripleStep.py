'''
Test cases:
(1) n = 0 -> 1
(2) n = 1 -> 1   {1}
(3) n = 2 -> 2   {1, 1} + {2}
(4) n = 3 -> 4   {1, 1, 1} + {1, 2} + {2, 1} + {3}
(5) n = 4 -> 7   {1, 1, 1, 1} + {1, 1, 2} + {1, 2, 1} + {2, 1, 1} + {1, 3} + {3, 1} + {4}
'''

class TripleStep():
    def __init__(self):
        return

    def triple_step(self, n, memo={}):
        if n in memo:
            return memo[n]

        if n < 0:
            return 0

        if n == 0:
            return 1

        memo[n] = self.triple_step(n-1, memo) + self.triple_step(n-2, memo) + self.triple_step(n-3, memo)

        return memo[n]


if __name__ == '__main__':
    f = TripleStep()
    v1 = f.triple_step(2)
    v2 = f.triple_step(3)
    v3 = f.triple_step(4)

    print(v1)
    print(v2)
    print(v3)
