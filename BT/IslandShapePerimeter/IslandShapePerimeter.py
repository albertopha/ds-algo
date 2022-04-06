from collections import deque

class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]:
                    return self.getPerimeter(matrix, row, col)
        return 0
    
    def getPerimeter(self, matrix, row, col):
        perimeter = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        queue = deque()
        queue.appendleft((row, col))

        while queue:
            r, c = queue.pop()

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dir_r, dir_c in dirs:
                nr, nc = dir_r + r, dir_c + c
                should_explore = True

                if nr < 0:
                    perimeter += 1
                    should_explore = False
                if nr >= len(matrix):
                    perimeter += 1
                    should_explore = False
                if nc < 0:
                    perimeter += 1
                    should_explore = False
                if nc >= len(matrix[0]):
                    perimeter += 1
                    should_explore = False
                if should_explore and matrix[nr][nc] == 0:
                    perimeter += 1
                    should_explore = False
                
                if should_explore and (nr, nc) not in visited:
                    queue.appendleft((nr, nc))

        return perimeter

        
