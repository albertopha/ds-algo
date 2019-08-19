# !
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        row_len = len(matrix)

        if row_len < 1:
            return 0

        col_len = len(matrix[0])

        if col_len < 1:
            return 0

        height_matrix = matrix[:]

        for row in range(row_len):
            self.maxArea(height_matrix, row)

    def maxArea(self, matrix, row):
        stack = list()

        for col in range(len(matrix[row])):
            if matrix[row][col] == '0':
                stack = []
                continue

            height = int(matrix[row][col]) if row == 0 else int(matrix[row-1][col]) + int(matrix[row][col])
            matrix[row][col] = str(height)

            if len(stack) == 0:
                stack.append(col)

            peek = stack[-1]
            if peek > height:
                popped = stack.pop(-1)


