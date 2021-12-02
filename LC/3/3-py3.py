"""
tmmzuxt
  ^
  ^
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        start = 0
        m = dict()
        max_len = 1
        
        for end in range(len(s)):
            if s[end] in m and m[s[end]] >= start:
                start = m[s[end]] + 1
            m[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len
