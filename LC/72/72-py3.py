"""
                horse -> ros
         /                   \ 
    orse -> os               orse -> ros
     /
  rse -> s
  /         \
se -> ""   se -> s
             |
           e -> ""
 
        
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word2) if not word1 else len(word1)
        
        return self.minDistanceMemo(word1, word2, 0, 0, [[-1 for _ in range(len(word2))] for _ in range(len(word1))])
    
    def minDistanceMemo(self, word1: str, word2: str, i1: int, i2: int, memo: List[List[int]]) -> int:
        if i1 >= len(word1) and i2 >= len(word2):
            return 0

        if i1 >= len(word1) or i2 >= len(word2):
            return len(word2) - i2 if i1 >= len(word1) else len(word1) - i1 
        
        if memo[i1][i2] != -1:
            return memo[i1][i2]
        
        if word1[i1] == word2[i2]:
            return self.minDistanceMemo(word1, word2, i1+1, i2+1, memo)
        
        insertion = 1 + self.minDistanceMemo(word1, word2, i1, i2+1, memo)
        deletion = 1 + self.minDistanceMemo(word1, word2, i1+1, i2, memo)
        replace = 1 + self.minDistanceMemo(word1, word2, i1+1, i2+1, memo)
        memo[i1][i2] = min(insertion, deletion, replace)
        return memo[i1][i2]
