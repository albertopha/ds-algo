class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'

        if n == 0:
            return result

        for i in range(1, n):
            result = self.interpret(result)

        return result

    @staticmethod
    def interpret(s):
        count = 1
        result = ''
        for i in range(len(s)):
            if i < len(s)-1 and s[i] == s[i+1]:
                count += 1
            else:
                result += str(count) + str(s[i])
                count = 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.interpret('11'))
    print(solution.interpret('1211'))
    print(solution.interpret('111221'))
    print(solution.countAndSay(6))
