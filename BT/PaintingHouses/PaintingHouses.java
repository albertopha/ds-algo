/*
[5, 3, 4],
[2, 1, 6],
[2, 3, 4],
[4, 3, 3]

Note: this is not the most optimal solution.
*/
import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int[][] dp = new int[matrix.length][matrix[0].length];
        for (int row = 0; row < dp.length; row++) Arrays.fill(dp[row], -1);
        return solve(matrix, 0, -1, dp);
    }

    private int solve(int[][] matrix, int row, int prevCol, int[][]dp) {
        if (row == matrix.length) return 0;
        if (prevCol > -1 && dp[row][prevCol] != -1) return dp[row][prevCol];

        int lowest = Integer.MAX_VALUE;
        for (int col = 0; col < matrix[0].length; col++) {
            if (prevCol == col) continue;
            int cost = matrix[row][col];
            lowest = Math.min(lowest, cost + solve(matrix, row + 1, col, dp));
        }

        if (prevCol > -1) {
            dp[row][prevCol] = lowest;
        }
        return lowest;
    }
}
