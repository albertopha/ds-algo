class Fib():
    def __init__(self):
        return

    def fib(self, n, memo={}):
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            return n

        memo[n] = self.fib(n-1, memo) + self.fib(n-2, memo)

        return memo[n]


if __name__ == '__main__':
    f = Fib()
    v1 = f.fib(2)
    v2 = f.fib(3)
    v3 = f.fib(9)

    print(v1)
    print(v2)
    print(v3)
