#!
class Parens:
    def __init__(self):
        return

    def parens(self, n):
        if n < 1:
            return ''

        perm = []
        init = '(' * n + ')' * n
        # self.parens_rec_brute(list(init), 0, len(init)-1, perm)
        self.parens_rec_optimized('', n, 0, perm)

        return perm

    def parens_rec_brute(self, s, start, end, perm):
        if start == end and self.parens_validate(s) and ''.join(s) not in perm:
            perm.append(''.join(s))
            return

        for i in xrange(start, end+1):
            s[start], s[i] = s[i], s[start]
            self.parens_rec_brute(s, start+1, end, perm)
            s[start], s[i] = s[i], s[start]

    def parens_rec_other(self, n):
        if n == 0:
            return ['']

        prev = self.parens_rec_other(n - 1)
        curr = []
        for p in prev:
            for i in range(len(p)):
                add_to_curr = self.add_paren(p, i)
                if add_to_curr not in curr:
                    curr.append(add_to_curr)
            add_to_curr = self.add_paren(p, len(p))
            if add_to_curr not in curr:
                curr.append(add_to_curr)
        return curr

    def parens_rec_optimized(self, s, left, right, perm):
        if left == 0 and right == 0:
            perm.append(s)

        if left > 0:
            self.parens_rec_optimized(s + '(', left-1, right+1, perm)

        if right > 0:
            self.parens_rec_optimized(s + ')', left, right-1, perm)


    @staticmethod
    def parens_validate(s):
        stack = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue

            curr = stack.pop()
            if curr == s[i]:
                stack.extend([curr, s[i]])
            elif curr != '(':
                return False

        return len(stack) == 0

    @staticmethod
    def add_paren(s, start):
        return s[0: start] + '()' + s[start:]


if __name__ == '__main__':
    parens = Parens()
    print(parens.parens_validate(''))
    print(parens.parens_validate(')'))
    print(parens.parens_validate('))'))
    print(parens.parens_validate('))(('))
    print(parens.parens_validate('()'))
    print(parens.parens_validate('(())'))

    print(parens.parens(1))
    print(parens.parens(2))
    print(parens.parens(3))

