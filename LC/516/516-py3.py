"""
    b | b | b | a | b |
b | 1 | 2 | 3 | 3 | 4 |
b |   | 1 | 2 | 2 | 3 |
b |       | 1 | 1 | 3 |
a |           | 1 | 2 |
b |               | 1 |
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(s)-1):
            dp[i][i+1] = 1 if s[i] != s[i+1] else 2
        
        for i in range(2, len(s)):
            row = 0
            col = i
            while row < len(s) - i:
                dp[row][col] = dp[row+1][col-1] + 2 if s[row] == s[col] else max(dp[row+1][col], dp[row][col-1])
                row += 1
                col += 1
        
        return dp[0][-1]
        
