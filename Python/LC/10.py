# !
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) > 0 and len(p) == 0:
            return False

        if len(s) == 0:
            if len(p) > 0 and p[0] == "*":
                return True

            if len(p) > 1 and p[1] == '*':
                return True

            else:
                return False

        dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        dp[0][0] = True

        for i in range(1, len(dp[0])):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s)):
            text = s[i - 1]
            for j in range(1, len(p)):
                pattern = p[j - 1]
                if text == pattern or pattern == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern == '*':
                    if p[j - 2] == '.' or p[j - 2] == text:
                        dp[i][j] = dp[i][j - 3] or dp[i - 1][j]
                else:
                    dp[i][j] = False

        return dp[len(s) - 1][len(p) - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatch('abcdfghj', 'a.*d'))
