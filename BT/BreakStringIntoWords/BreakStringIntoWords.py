"""
thequickbrownfox

q: [quick]
b: [brown]
t: [the]
f: [fox]
"""
from collections import defaultdict

class Solution:
    def solve(self, words, s):
        if not words or not s:
            return False
        
        dp = [None] * len(s)
        char_map = defaultdict(set)
        for word in words:
            char_map[word[0]].add(word)
        return self.helper(char_map, s, 0, dp)

    def helper(self, char_map, s, start, dp):
        if start >= len(s):
            return True

        if dp[start] is not None:
            return dp[start]
        
        if s[start] not in char_map:
            return False
        
        for word in char_map[s[start]]:
            if s.startswith(word, start) and\
                self.helper(char_map, s, start+len(word), dp):
                return True
        dp[start] = False
        return False 
