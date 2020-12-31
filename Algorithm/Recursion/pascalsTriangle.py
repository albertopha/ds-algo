class PascalsTriangle:
    def __init__(self):
        self.pascals_triangle = []

    def create(self, numRows):
        pascals_triangle = []

        self.createRec(numRows, pascals_triangle)
        print(pascals_triangle)
        self.pascals_triangle = pascals_triangle
        return pascals_triangle

    def createRec(self, numRows, pt):
        if numRows == 1:
            pt.append([1])
            return

        self.createRec(numRows-1, pt)

        new_row = [1 for _ in range(numRows)]
        prev_row = pt[numRows-2]

        for col in range(numRows):
            if col <= 0 or col >= len(prev_row):
                continue

            new_row[col] = prev_row[col-1] + prev_row[col]

        pt.append(new_row)


if __name__ == '__main__':
    pt = PascalsTriangle()
    pt.create(5)