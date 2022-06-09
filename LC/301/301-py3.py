"""
()())()
                      /       \
                  ()())()    )())()
                  /    \
               
                  
1. Recursion
2. Starting with ) => return false
3. if minimum paren found => record

(())()
"""
from typing import List, Tuple
import heapq

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s or self.isValid(s):
            return [] if not s else [s]
        parens = []
        self.helper(s, 0, parens)
        return list(set(map(lambda p: p[1], parens)))
    
    def helper(self, s: str, removeCount: int, parens: List[Tuple]) -> None:
        if not s:
            if not parens:
                heapq.heappush(parens, (removeCount, ""))
            return 
        
        if parens and parens[0][0] < removeCount:
            return
        
        if self.isValid(s):
            if not parens or removeCount < parens[0][0]:
                parens.clear()
                parens.append((removeCount, s))
            else:
                heapq.heappush(parens, (removeCount, s))
            return
        
        for i in range(len(s)):
            if s[i] not in ("(", ")"):
                continue
            substr = s[0:i] + s[i+1:]
            self.helper(substr, removeCount+1, parens)
    
    def isValid(self, s: str) -> bool:
        open_paren = 0
        for char in s:
            if char not in ("(", ")"):
                continue
                
            if char == '(':
                open_paren += 1
                continue
            
            if open_paren == 0:
                return False
            
            open_paren -= 1
        
        return open_paren == 0

s = Solution()
print(s.removeInvalidParentheses("()(((((((()"))
