class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        return self.divide(matrix, target)

    def divide(self, matrix, target):
        if not matrix:
            return False

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target

        rowLen = len(matrix)
        rowMid = rowLen // 2
        colLen = len(matrix[0])
        colMid = colLen // 2

        # Search if target is in mid points
        row = 0
        while row < rowLen:
            if matrix[row][colMid] == target:
                return True
            row += 1

        col = 0
        while col < colLen:
            if matrix[rowMid][col] == target:
                return True
            col += 1

        middle_point = matrix[rowMid][colMid]
        print("mid_point = ", middle_point)
        if middle_point > target:
            cut = matrix[0:rowMid]
            if colMid > 0:
                cut = [cut[i][0:colMid] for i in range(len(cut))]
            print("**** bottom: ", cut)
            return self.divide(cut, target)
        else:
            cut = matrix[rowMid:]

            if colMid > 0:
                cut = [cut[i][colMid:] for i in range(len(cut))]
            print("**** top: ", cut)
            return self.divide(cut, target)


if __name__ == '__main__':
    s = Solution()
    D = [[1,   4,  7, 11, 15], [2,   5,  8, 12, 19], [3,   6,  9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    E = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    B = [[1], [2], [3], [4], [5]]
    print(s.searchMatrix(E, 5))
    # print(s.searchMatrix(D, 24))
    # print(s.searchMatrix(D, 5))
    # print(s.searchMatrix(D, 105))
    # print(s.searchMatrix(D, 0))
    # print(s.searchMatrix(B, 0))
    # print(s.searchMatrix(B, 5))
    # print(s.searchMatrix(B, 1))

