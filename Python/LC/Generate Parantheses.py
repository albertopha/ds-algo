class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        self.generateParBT(n, results, "(", 1)
        return results

    def generateParBT(self, n, results, current, count):
        if count < 0:
            return

        if len(current) == n * 2:
            if self.is_valid(current):
                results.append(current)
            return

        self.generateParBT(n, results, current + "(", count+1)
        if count > 0:
            self.generateParBT(n, results, current + ")", count-1)

    def is_valid(self, current):
        stack = []
        for c in current:
            if c == "(":
                stack.append(c)
                continue
            if c == ")" and len(stack) == 0:
                return False
            stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))
    print(s.generateParenthesis(2))
    print(s.generateParenthesis(3))
    print(s.generateParenthesis(4))
