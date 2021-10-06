"""
abcde
a b c c c c c c d
^
    ^
acbcd
^
 ^
                acbcd
                
   a b c c c c c d
---------------------
a |1|1|1|1|1|1|1|1| 
c |1|1|2|2|2|2|2|2|
b |1|2|2|2|2|2|2|2|
c |1|2|3|3|3|3|3|3|
d |1|2|3|3|3|3|3|4|
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        
        m, n = len(text1), len(text2)
        dp = [[0]*m for _ in range(n)]
        
        for col in range(m):
            if text1[col] == text2[0]:
                dp[0][col] = 1
            dp[0][col] = max(dp[0][col], dp[0][col-1]) if col > 0 else dp[0][col]
        
        for row in range(n):
            if text1[0] == text2[row]:
                dp[row][0] = 1
            dp[row][0] = max(dp[row][0], dp[row-1][0]) if row > 0 else dp[row][0]
        
        for row in range(1, n):
            for col in range(1, m):
                if text1[col] == text2[row]:
                    dp[row][col] = dp[row-1][col-1] + 1
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
        
        return dp[-1][-1]