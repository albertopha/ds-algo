from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = self.traverseBFS(grid)
        if self.check(grid):
            return count

        return -1

    def traverseBFS(self, grid: List[List[int]]) -> int:
        queue = []
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))

        while len(queue) > 0:
            inner_queue = list(queue)
            queue = []
            while len(inner_queue) > 0:
                crow, ccol = inner_queue.pop(0)

                if grid[crow][ccol] != 2:
                    continue

                if ccol-1 >= 0 and grid[crow][ccol-1] == 1:
                    grid[crow][ccol-1] = 2
                    queue.append((crow, ccol-1))

                if ccol+1 < len(grid[0]) and grid[crow][ccol+1] == 1:
                    grid[crow][ccol+1] = 2
                    queue.append((crow, ccol+1))

                if crow-1 >= 0 and grid[crow-1][ccol] == 1:
                    grid[crow-1][ccol] = 2
                    queue.append((crow-1, ccol))

                if crow+1 < len(grid) and grid[crow+1][ccol] == 1:
                    grid[crow+1][ccol] = 2
                    queue.append((crow+1, ccol))

            count += 1

        return count-1 if count > 0 else count

    def check(self, grid: List[List[int]]) -> bool:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(s.orangesRotting([[0,2]]))
    print(s.orangesRotting([[0]]))
