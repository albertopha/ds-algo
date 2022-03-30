"""
1 3 3
1   2
7 3 1

                    1
                  /   \   
                 1     3
                / \
               4   5 ()
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        for col in range(1, len(grid[0])):
            grid[0][col] += grid[0][col-1]
            
        for row in range(1, len(grid)):
            grid[row][0] += grid[row-1][0]
            
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        return grid[-1][-1]
