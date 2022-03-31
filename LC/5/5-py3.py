class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        max_start, max_end = 0, 0
        for i in range(1, len(s)):
            start, end = self.expand(s, i, i)
            #print(i, ', start = ', start, ', end = ', end)
            
            if end - start + 1 > max_end - max_start + 1:
                max_start, max_end = start, end
        
        for i in range(len(s)-1):
            start, end = self.expand(s, i, i+1)
            if end - start + 1 > max_end - max_start + 1:
                max_start, max_end = start, end
                
        return s[max_start:max_end+1]
    
    
    def expand(self, s: str, start: int, end: int) -> tuple:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start-=1
            end+=1
        return max(start+1, 0), min(end-1, len(s)-1)
