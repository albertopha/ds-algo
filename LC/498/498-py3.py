from collections import deque
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        output = []
        is_reversed = True
        for c in range(n):
            output.extend(self.traverse(mat, 0, c, is_reversed)) 
            is_reversed = not is_reversed 
        for r in range(1, m):
            output.extend(self.traverse(mat, r, n-1, is_reversed))
            is_reversed = not is_reversed
            
        return output
    
    def traverse(self, mat: List[List[int]], row: int, col: int, is_reversed: bool) -> List[int]:
        m, n = len(mat), len(mat[0])
        traversed = deque() 
        
        while row < m and col >= 0:
            if is_reversed:
                traversed.appendleft(mat[row][col])
            else:
                traversed.append(mat[row][col])
            row += 1
            col -= 1
        return traversed
      
