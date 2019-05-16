#!
class EightQueens:
    def __init__(self):
        self.chess = [[0 for _ in range(8)] for _ in range(8)]

    def eight_queens_rec(self, col=0, N=8):
        if col >= N:
            return True

        for row in range(N):

            if self.validate(self.chess, row, col, N):
                self.chess[row][col] = 1

                if self.eight_queens_rec(col+1, N):
                    return True

                self.chess[row][col] = 0

        return False

    @staticmethod
    def validate(chessboard, row, col, N):
        for i in range(col):
            if chessboard[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if chessboard[i][j] == 1:
                return False

        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if chessboard[i][j] == 1:
                return False

        return True

    def print_board(self):
        print(self.chess)


if __name__ == '__main__':
    eq = EightQueens()
    eq.eight_queens_rec()
    eq.print_board()