"""
                            a     b   b   a
            /               |       \
          ab[1]            ab[2]     aa[3]
       /        \         /     \
     abb[2]     aba[3]   aba[3]  ""
    /  \       /  \
 abba[3]   ""    ""   ""
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        count = 0
        
        for i in range(len(s)):
            count += self.expand(s, i, i)
        
        for i in range(len(s)-1):
            count += self.expand(s, i, i+1)
        
        return count
    
    def expand(self, s: str, start: int, end: int) -> int:
        count = 0
        while start >= 0 and end < len(s) and s[start] == s[end]:
            count += 1
            start -= 1
            end += 1
        return count
