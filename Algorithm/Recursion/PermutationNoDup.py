#!
class PermutationNoDup:
    def __init__(self):
        return

    def permutation_without_dup(self, s):
        perm = []

        if len(s) < 2:
            return s

        # self.permutation_rec_brute(s, '', perm)
        self.permutation_rec(list(s), 0, len(s)-1, perm)
        return perm

    def permutation_rec_brute(self, s, curr, perm):
        if s == '':
            perm.append(curr)
            return

        for i in range(len(s)):
            new_curr = curr + s[i]
            if i == 0:
                self.permutation_rec(s[i+1:], new_curr, perm)
            elif i == len(s)-1:
                self.permutation_rec(s[0:i], new_curr, perm)
            else:
                self.permutation_rec(s[0:i]+s[i+1:], new_curr, perm)

    def permutation_rec(self, s, start, end, perm):
        if start == end:
            perm.append(''.join(s))
            return

        for i in range(start, end+1):
            s[start], s[i] = s[i], s[start]
            self.permutation_rec(s, start+1, end, perm)
            s[start], s[i] = s[i], s[start]


if __name__ == '__main__':
    pnd = PermutationNoDup()
    perms1 = pnd.permutation_without_dup('abc')
    perms2 = pnd.permutation_without_dup('abcd')

    print(perms1)
    print(perms2)