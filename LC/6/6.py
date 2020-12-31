#! Re - J
import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s

        return self.optimized(s, numRows)

    @staticmethod
    def optimized(s: str, num_rows: int) -> str:
        l = [''] * num_rows
        direction, ind = 1, 0

        for ch in s:
            l[ind] += ch
            if ind == 0:
                direction = 1
            if ind == num_rows - 1:
                direction = -1

            ind += direction

        return ''.join(l)

    @staticmethod
    def brute_force(s: str, num_rows: int) -> str:
        size = num_rows * math.floor(len(s) * num_rows / (2 * num_rows - 1)) if len(s) > num_rows else 1
        matrix = [[0 for _ in range(size)] for _ in range(num_rows)]

        flag = False
        row, col, i = 0, 0, 0

        while i < len(s):
            if not flag:
                while row < num_rows and i < len(s):
                    matrix[row][col] = s[i]
                    row += 1
                    i += 1
                row -= 2
                col += 1
                flag = True
            else:
                while row >= 0 and i < len(s):
                    matrix[row][col] = s[i]
                    row -= 1
                    col += 1
                    i += 1
                row += 2
                col -= 1
                flag = False

        # print(matrix)
        result = ''
        for rows in range(num_rows):
            for cols in range(size):
                if matrix[rows][cols] != 0:
                    result += matrix[rows][cols]

        return result


if __name__ == '__main__':
    s = Solution()

    converted0 = s.convert("PAYPALISHIRING", 3)
    print(len(converted0))
    print(converted0)
    print(converted0 == 'PAHNAPLSIIGYIR')

    converted1 = s.convert('PAYPALISHIRING', 4)
    print(len(converted1))
    print(converted1)
    print(converted1 == 'PINALSIGYAHRPI')

    converted2 = s.convert('A', 2)
    print(len(converted2))
    print(converted2)
    print(converted2 == 'A')

    converted3 = s.convert('', 2)
    print(len(converted3))
    print(converted3)
    print(converted3 == '')

    converted4 = s.convert('ABCD', 0)
    print(len(converted4))
    print(converted4)
    print(converted4 == 'ABCD')

    converted5 = s.convert('AB', 1)
    print(len(converted5))
    print(converted5)
    print(converted5 == 'AB')

    converted6 = s.convert("sxztrmivgdyiwnmrtnmpwsgjemfyiwwatvvmjdkphiafymyrbkgxemiianikjekfbfrllbaumczkozdpllopzwzzkhlvnva", 87)
    print(len(converted6))
    print(converted6)
