"""
PAHNAPLSIIGYIR
^

dir = "down" | "up"

a       i
b     h j
c   g   k
d f     l m
e       n

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or not numRows:
            return s
        
        output = [[] for _ in range(numRows)]
        
        i = 0
        while i < len(s):
            for down in range(numRows):
                if i >= len(s):
                    break
                output[down].append(s[i])
                i += 1
            
            for up in range(numRows-2,0,-1):
                if i >= len(s):
                    break
                output[up].append(s[i])
                i += 1
        result = []
        for row in range(len(output)):
            result.extend(output[row])
        return "".join(result)
                
            
