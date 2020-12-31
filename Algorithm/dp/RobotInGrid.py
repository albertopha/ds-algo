#!
class RobotInGrid():
    def __init__(self, r, c, off_limits):
        self.grid = [0 for _ in range(r)]
        arr = [0 for _ in range(c)]

        for i in range(r):
            self.grid[i] = arr[:]

        for coordinate in off_limits:
            x = coordinate[0]
            y = coordinate[1]
            self.grid[x][y] = -1

        print(self.grid)

    def find_path(self):
        path = []
        if len(self.grid) == 0 or self.grid[0][0] == -1 or self.grid[len(self.grid)-1][len(self.grid)-1] == -1:
            return path

        self.find_path_rec(len(self.grid)-1, len(self.grid[0])-1, path)
        return path

    # memo = set of invalid path (in tuple)
    def find_path_rec(self, row, col, path, memo=set()):
        if row < 0 or col < 0 or self.grid[row][col] == -1:
            return False

        if (row, col) in memo:
            return False

        if (row == 0 and col == 0) or\
                self.find_path_rec(row-1, col, path, memo) or\
                self.find_path_rec(row, col-1, path, memo):
            path.append([row, col])
            return True

        memo.add((row, col))
        return False


if __name__ == '__main__':
    grid = RobotInGrid(4, 4, [[0, 2], [0, 3], [1, 0], [1, 3], [2, 2], [3, 0]])
    print(grid.find_path())

