# Re - J
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        counter = 1
        result = [[-1 for _ in range(n)] for _ in range(n)]
        row_start, col_start, row_end, col_end = 0, 0, n, n

        while row_start < row_end and col_start < col_end:
            for i in range(col_start, col_end):
                result[row_start][i] = counter
                counter += 1

            row_start += 1

            for i in range(row_start, row_end):
                result[i][col_end-1] = counter
                counter += 1

            col_end -= 1

            for i in range(col_end-1, col_start, -1):
                result[row_end-1][i] = counter
                counter += 1

            row_end -= 1

            for i in range(row_end, row_start-1, -1):
                result[i][col_start] = counter
                counter += 1

            col_start += 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
    print(s.generateMatrix(4))
    print(s.generateMatrix(5))