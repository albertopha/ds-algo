class Solution:
    def solveSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            return False
        self.runSudoku(board, 0, 0)
        return board
        
    def runSudoku(self, board: List[List[str]], row: int, col: int) -> bool:
        m, n = len(board), len(board[0])
        
        if row >= m:
            return True
        
        if col >= n:
            return self.runSudoku(board, row+1, 0)
        
        if board[row][col] != '.':
            return self.runSudoku(board, row, col+1)
        
        for value in '123456789':
            board[row][col] = value
            if self.isValid(board, row, col) and self.runSudoku(board, row, col+1):
                return True
            board[row][col] = '.';
            
        return False 
    
    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        m, n = len(board), len(board[0])
        seen = set()
        
        # Checking columns
        for c in range(n):
            if board[row][c] == '.':
                continue
            if board[row][c] in seen:
                return False
            seen.add(board[row][c])
        
        # Checking rows
        seen = set()
        for r in range(m):
            if board[r][col] == '.':
                continue
            if board[r][col] in seen:
                return False
            seen.add(board[r][col])
        
        # Checking 3x3
        seen = set()
        row_start, col_start = row // 3 * 3, col // 3 * 3
        for r in range(row_start, row_start+3):
            for c in range(col_start, col_start+3):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        return True
                
