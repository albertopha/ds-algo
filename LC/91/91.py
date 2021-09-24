from collections import defaultdict
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        return self.numDecodingsHelper(s, defaultdict(lambda x:0))
        
    def numDecodingsHelper(self, s, memo):
        if not s:
            return 1
        
        if s[0] == "0":
            return 0
        
        if s in memo:
            return memo[s]
        
        first = 0
        second = 0
        
        if len(s) > 0:
            first = self.numDecodingsHelper(s[1:], memo)
        
        if len(s) > 1 and int(s[0:2]) <= 26:
            second = self.numDecodingsHelper(s[2:], memo)
            
        memo[s] = first + second
        return memo[s]