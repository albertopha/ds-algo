#!
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.longest_valid_paren_opt(s)

    def longest_valid_paren_opt(self, s):
        stack = [-1]
        result = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()

                if len(stack) > 0:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)

        return result

    def longest_valid_paren_brute(self, s, start, end):
        if start >= end:
            return 0

        if self.validate(s, start, end):
            return end - start

        return max(self.longest_valid_paren_brute(s, start+1, end),
                   self.longest_valid_paren_brute(s, start, end-1))

    @staticmethod
    def validate(s, start, end):
        stack = []
        for i in range(start, end):
            if s[i] == '(':
                stack.append(s[i])
            elif len(stack) == 0:
                return False
            else:
                stack.pop()

        if len(stack) > 0:
            return False

        return True


if __name__ == '__main__':
    lvp = Solution()
    print(lvp.validate("()", 0, 2))
    print(lvp.validate("(()", 0, 3))

    print(lvp.longestValidParentheses("()"))
    print(lvp.longestValidParentheses("(()"))
    print(lvp.longestValidParentheses("(())"))
    print(lvp.longestValidParentheses(")()())"))
    print(lvp.longestValidParentheses(")(((((()())()()))()(()))("))
