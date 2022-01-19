"""
Using first row and first column as a flag whether that particular row or col needs to be zero.
Caveat:
[1, 2, 3, 4]
[5, 0, 7, 8]
[0,10,11,12]
[13,14,15,0]

[0, 0, 3, 0]
[0, 0, 7, 8]
[0,10,11,12]
[0,14,15,0]

[0, 0, 3, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix[0]) == 0:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Flag to set col zero
        is_first_col_zero = False
        
        for row in range(m):
            if matrix[row][0] == 0:
                is_first_col_zero = True
                
            # Should start the column at index of 1
            # Otherwise, first row gets corrupted
            # and won't be able to figure out whether
            # the first row needs to be zero or not
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # Check every cell except the ones in the first row and col
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        # matrix[0][0] is used as a flag for the first row
        if matrix[0][0] == 0:
            for col in range(n):
                matrix[0][col] = 0
            
        if is_first_col_zero:
            for row in range(m):
                matrix[row][0] = 0
