class LongestPalindrome(object):
    def longest_palindrome_opt(self, s):
        palindrome = ''
        table = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            palindrome = s[i]
            table[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                palindrome = s[i:i + 2]
                table[i][i + 1] = True

        for k in range(2, len(s)):
            for i in range(len(s)):
                j = i + k
                if i < len(s) and j < len(s) and s[i] == s[j] and table[i + 1][j - 1]:
                    curr = s[i:j + 1]
                    if len(curr) > len(palindrome):
                        palindrome = curr

                    table[i][j] = True

        return palindrome

    def longest_palindrome_brute(self, s):
        if len(s) < 1:
            return s

        start, end = 0, len(s)
        longest_palindrome = [s[0]]
        self.longest_palidrome_brute_rec(s, start, end, longest_palindrome)
        return longest_palindrome[0]

    def longest_palidrome_brute_rec(self, s, start, end, longest_palindrome):
        if start >= end:
            return

        if self.check_palindrome(s[start:end]) and len(longest_palindrome[0]) < len(s[start:end]):
            longest_palindrome[0] = s[start:end]
        else:
            self.longest_palidrome_brute_rec(s, start+1, end, longest_palindrome)
            self.longest_palidrome_brute_rec(s, start, end-1, longest_palindrome)

    @staticmethod
    def check_palindrome(s):
        start, end = 0, len(s)-1

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True


if __name__ == '__main__':
    lp = LongestPalindrome()
    print(lp.check_palindrome("babad"))
    print(lp.longest_palindrome_brute("babad"))
    print(lp.longest_palindrome_opt("cbbd"))
    print(lp.longest_palindrome_opt("babaddtattarrattatddetartrateedredividerb"))
    print(lp.longest_palindrome_opt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))


