class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board[0]) == 0:
            return False
        
        if not word:
            return True
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                visited = set()
                visited.add((row, col))
                if board[row][col] == word[0] and\
                    self.backtrack(board, row, col, word, 1, visited):
                    return True
        return False
    
    def backtrack(self, board: List[List[str]], row: int, col: int, word: str, pos: int, visited: set) -> bool:
        if pos >= len(word):
            return True
        
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for dir_row, dir_col in dirs:
            new_row, new_col = dir_row + row, dir_col + col
            
            coord = (new_row, new_col)
            if new_row < 0 or new_row >= len(board) or\
                new_col < 0 or new_col >= len(board[0]) or\
                coord in visited or\
                board[new_row][new_col] != word[pos]:
                continue
            
            visited.add(coord)
            if self.backtrack(board, new_row, new_col, word, pos+1, visited):
                return True
            visited.remove(coord)
        return False
            
