from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = max(area, self.getArea(grid, row, col))
        return area
    
    def getArea(self, grid: List[List[int]], row: int, col: int) -> int:
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        area = 1
        grid[row][col] = 0
        queue = deque([(row, col)])
        
        while queue:
            r, c = queue.popleft()
            
            for dir_row, dir_col in dirs:
                new_row, new_col = r + dir_row, c + dir_col
                
                if 0 <= new_row < len(grid) and\
                    0 <= new_col < len(grid[0]) and\
                    grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 0
                        area += 1
                        queue.append((new_row, new_col))

        return area
                
