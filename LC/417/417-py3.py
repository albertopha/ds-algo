from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        output = []
        pacific_visited = [[False for _ in range(n)] for _ in range(m)]
        atlantic_visited = [[False for _ in range(n)] for _ in range(m)]
        
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Horizontal
        for col in range(n):
            pacific_queue.append((0, col))
            atlantic_queue.append((m-1, col))
            pacific_visited[0][col] = True
            atlantic_visited[m-1][col-1] = True
        
        # Vertical 
        for row in range(m):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, n-1))
            pacific_visited[row][0] = True
            atlantic_visited[row][n-1] = True
        
        self.explore(heights, pacific_queue, pacific_visited)
        self.explore(heights, atlantic_queue, atlantic_visited)
        
        for row in range(m):
            for col in range(n):
                if pacific_visited[row][col] and atlantic_visited[row][col]:
                    output.append([row, col])
        return output
    
    def explore(self, heights: List[List[int]], queue: deque, visited: List[List[int]]) -> None:
        m, n = len(heights), len(heights[0])
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        
        while queue:
            r, c = queue.pop()
            
            for dir_row, dir_col in dirs:
                new_row, new_col = r + dir_row, c + dir_col

                if new_row < 0 or new_row >= m or\
                    new_col < 0 or new_col >= n or\
                    heights[r][c] > heights[new_row][new_col] or\
                    visited[new_row][new_col]:
                    continue

                visited[new_row][new_col] = True
                queue.appendleft((new_row, new_col))
                    
            
