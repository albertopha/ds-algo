class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        output = [0]*(n+1)
        output[1] = 1
        
        for i in range(2, n+1):
            output[i] = 1 if i % 2 != 0 else 0
            output[i] += output[i//2]
        
        return output
