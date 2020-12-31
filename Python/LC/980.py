"""
WATCH OUT FOR THE COMPLEXITY CALCULATION!

[[1,0,0,0],
 [0,0,0,0],
 [0,0,2,-1]]

Brute force:
1. Iterate through the grid:
    a. find the start point.
    b. find the end point and change end point to 0.
    c. count the number of obstacles
    
2. Using the dfs backtracking to find the end point.
    a. Each recursion (move), increment the count.
    b. Once reached to the end point, increment the output (result)
        only if the count === (# of grid - obstacles - start point).
        
Time: O(3^N), only start point requires 4 directions to consider. After first move,
    we only consider 3 directions to traverse.
Space: O(N), due to recursion stack (no extra space needed due to the in-place technique).
"""
class Solution(object):
    def unquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid[0]) == 0:
            return 0
        
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        return self.bruteForce(grid)
    
    def bruteForce(self, grid):
        start = [0, 0]
        end = [0, 0]
        obstacles = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start[0], start[1] = row, col
                
                if grid[row][col] == -1:
                    obstacles += 1
                
                if grid[row][col] == 2:
                    end[0], end[1] = row, col
                    grid[row][col] = 0
        
        output = [0]
        # total = number of cells - # of obstacles - start position
        total_count = len(grid) * len(grid[0]) - obstacles - 1
        
        if total_count <= 0:
            return 1 if total_count == 0 else 0
        
        self.backtrack(grid, start[0], start[1], end, total_count, 0, output)
        return output[0]
    
    def backtrack(self, grid, row, col, end, total_count, count, output):
        if row == end[0] and col == end[1]:
            if total_count == count:
                output[0] += 1
            return
        
        for dir_row, dir_col in self.directions:
            new_row, new_col = row + dir_row, col + dir_col
            
            if 0 <= new_row < len(grid) and\
                0 <= new_col < len(grid[0]) and\
                grid[new_row][new_col] != -1 and\
                grid[new_row][new_col] != 1:
                    grid[new_row][new_col] = 1
                    self.backtrack(grid, new_row, new_col, end, total_count, count + 1, output)
                    grid[new_row][new_col] = 0
