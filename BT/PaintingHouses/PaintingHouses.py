class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        
        for row in range(m - 2, -1, -1):
            next_list = matrix[row+1][:]
            m1, m2 = self.getTwoMins(next_list)

            for col in range(n):
                matrix[row][col] += m1[1] if m1[0] != col else m2[1]
        
        return min(matrix[0])
    
    def getTwoMins(self, l):
        m1, m2 = None, None

        for i, val in enumerate(l):
            if m1 is None:
                m1 = (i, val)
                continue

            if m2 is None or val < m2[1]:
                m2 = (i, val)
            
            if m2[1] < m1[1]:
                m1, m2 = m2, m1

        return m1, m2
