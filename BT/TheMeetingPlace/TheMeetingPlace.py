from collections import deque

class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]:
            return -1
        
        queue = deque()
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 2:
                    queue.append((row, col))
                    matrix[row][col] = 0
                elif matrix[row][col] == 1:
                    matrix[row][col] = -1
        
        while queue:
            row, col = queue.pop()
            self.bfs(matrix, row, col)
        
        output = m * n
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == -1 or\
                    matrix[row][col] == 0:
                    continue
                output = min(output, matrix[row][col])
        return output if output != m * n else 0
        
    def bfs(self, matrix, row, col):
        m, n = len(matrix), len(matrix[0])
        queue = deque([(row, col, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]

        while queue:
            r, c, count = queue.popleft() 
            matrix[r][c] += count

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or\
                    nc < 0 or nc >= n or\
                    visited[nr][nc] or\
                    matrix[nr][nc] == -1:
                    continue
                
                visited[nr][nc] = True
                queue.append((nr, nc, count+1))
