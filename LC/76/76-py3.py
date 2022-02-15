"""
ADOBACODEBANC
      ^
            ^

unique_char = 1
{
    A: 0,
    B: 0,
    C: 1
}

min = 5

"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ""
        
        counter = Counter(t)
        unique_char_count = len(counter)
        min_left = 0
        min_right = len(s) - 1
        
        l = 0
        found = False
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] == 0:
                    unique_char_count -= 1
            
            while l <= r and unique_char_count == 0:
                if s[l] in counter:
                    if counter[s[l]] == 0:
                        unique_char_count += 1
                    counter[s[l]] += 1
                
                if r - l <= min_right - min_left:
                    found = True
                    min_left, min_right = l, r
                    
                l += 1
        
        return s[min_left:min_right+1] if found else "" 
