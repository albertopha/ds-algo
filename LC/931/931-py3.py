class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        for row in range(1, m):
            for col in range(n):
                first = matrix[row-1][max(0, col-1)]
                second = matrix[row-1][col]
                third = matrix[row-1][min(n-1, col+1)]
                matrix[row][col] += min(first, second, third)
        
        return min(matrix[-1])
            
