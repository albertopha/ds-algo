import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        
        int m = matrix.length;
        int n = matrix[0].length;
        for (int col = 1; col < n; col++) matrix[0][col] += matrix[0][col-1];
        for (int row = 1; row < m; row++) matrix[row][0] += matrix[row-1][0];
        for (int row = 1; row < m; row++) {
            for (int col = 1; col < n; col++) {
                matrix[row][col] += Math.max(matrix[row-1][col], matrix[row][col-1]);
            }
        }
        return matrix[m-1][n-1];
    }
}
