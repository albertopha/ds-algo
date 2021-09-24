"""
                    "1255"
                    /   \
                  "1"   "12"
                 /
                "2"
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        if s[0] == "0":
            return 0
        
        dp = [-1] * len(s)
        return self.numDecodingsRecurse(s, 0, dp)
        
    def numDecodingsRecurse(self, s: str, i: int, dp: List[int]) -> int:
        if i == len(s):
            return 1 if i == len(s) else 0
        
        if dp[i] != -1:
            return dp[i]
        
        if s[i] == "0":
            return 0
        
        count = self.numDecodingsRecurse(s, i+1, dp)
        if i < len(s)-1 and int(s[i:i+2]) <= 26:
            count += self.numDecodingsRecurse(s, i+2, dp)
        dp[i] = count
        return count