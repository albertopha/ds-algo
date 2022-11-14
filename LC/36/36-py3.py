class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            return False
        return self.areRowsValid(board) and\
            self.areColumnsValid(board) and\
            self.areBoxesValid(board)
        
    
    def areRowsValid(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        for col in range(n):
            seen = set()
            for row in range(m):
                value = board[row][col]
                if value == '.':
                    continue
                if value in seen:
                    return False
                seen.add(value)
        return True
    
    def areColumnsValid(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        for row in range(m):
            seen = set()
            for col in range(n):
                value = board[row][col]
                if value == '.':
                    continue
                if value in seen:
                    return False
                seen.add(value)
        return True
    
    def areBoxesValid(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                row_start, col_start = box_row*3, box_col*3
                for row in range(row_start, row_start+3):
                    for col in range(col_start, col_start+3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
        return True
                
