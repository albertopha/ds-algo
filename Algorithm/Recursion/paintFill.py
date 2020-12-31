#!
class PaintFill:
    def __init__(self, screen):
        self.screen = screen

    def paint_fill_brute(self, row, col, new_color):
        if row < 0 or col < 0\
            or row >= len(self.screen)\
                or col >= len(self.screen[0]):
            return

        curr_color = self.screen[row][col]
        self.visit_each_cell(row, col, curr_color, new_color)

    def visit_each_cell(self, row, col, curr_color, new_color):
        if row < 0 or col < 0\
            or row >= len(self.screen)\
            or col >= len(self.screen[0])\
                or self.screen[row][col] != curr_color:
            return

        self.screen[row][col] = new_color
        self.visit_each_cell(row, col-1, curr_color, new_color)
        self.visit_each_cell(row-1, col, curr_color, new_color)
        self.visit_each_cell(row, col+1, curr_color, new_color)
        self.visit_each_cell(row+1, col, curr_color, new_color)

    def get_screen(self):
        return self.screen


if __name__ == '__main__':
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 0],
              [1, 0, 0, 1, 1, 0, 1, 1],
              [1, 2, 2, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 2, 2, 0],
              [1, 1, 1, 1, 1, 2, 1, 1],
              [1, 1, 1, 1, 1, 2, 2, 1],
              ]
    pf = PaintFill(screen)
    pf.paint_fill_brute(5, 3, 15)
    print(pf.get_screen())