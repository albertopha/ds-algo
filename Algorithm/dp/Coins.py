class Coins():
    def __init__(self):
        return

    def get_coins(self, n, memo={}):
        if n in memo:
            return memo[n]

        if n < 0:
            return 0

        if n == 0:
            return 1

        memo[n] = self.get_coins(n-25) + self.get_coins(n-10) + self.get_coins(n-5) + self.get_coins(n-1)
        return memo[n]


if __name__ == '__main__':
    c = Coins()
    print(c.get_coins(1))
    print(c.get_coins(25))
    print(c.get_coins(40))
    print(c.get_coins(125))

