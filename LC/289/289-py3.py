class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        for row in range(m):
            for col in range(n):
                neighbours = self.getNeighbourCount(board, col, row)
                
                if (board[row][col] == 0 or board[row][col] == 2) and neighbours == 3:
                    board[row][col] = 2
                elif (board[row][col] == 1 or board[row][col] == -1) and (neighbours < 2 or neighbours > 3):
                    board[row][col] = -1
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0
    
    def getNeighbourCount(self, board, col, row) -> int:
        m, n = len(board), len(board[0])
        dirs = [
            [-1, -1], [0, -1], [1, -1],
            [-1, 0], [1, 0],
            [-1, 1], [0, 1], [1, 1]
        ]
        
        count = 0
        for dc, dr in dirs:
            nc, nr = dc + col, dr + row
            
            if 0 <= nr < m and 0 <= nc < n and (board[nr][nc] == 1 or board[nr][nc] == -1):
                count += 1
        return count
      
"""
Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously:
You cannot update some cells first and then use their updated values to update other cells.

In this question, we represent the board using a 2D array. In principle, the board is infinite,
which would cause problems when the active area encroaches upon the border of the array
(i.e., live cells reach the border). How would you address these problems?
"""
