class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n, count = len(matrix), len(matrix[0]), 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for col in range(n):
            dp[0][col] = int(matrix[0][col])
            count = max(count, dp[0][col])
            
        for row in range(m):
            dp[row][0] = int(matrix[row][0])
            count = max(count, dp[row][0])
            
        for row in range(1, m):
            for col in range(1, n):
                if int(matrix[row][col]) == 0:
                    continue
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
                count = max(count, dp[row][col])
        return count * count if count > 1 else count
    
