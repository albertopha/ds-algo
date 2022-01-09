import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        Integer[][] dp = new Integer[matrix.length][matrix[0].length];
        return solve(matrix, 0, -1, dp);
    }

    private int solve(int[][] matrix, int row, int prevCol, Integer[][] dp) {
        if (row >= matrix.length) return 0;
        if (prevCol >= 0 && dp[row][prevCol] != null) return dp[row][prevCol]; 

        int sum = Integer.MAX_VALUE;
        for (int col = 0; col < matrix[0].length; col++) {
            if (col == prevCol) continue;
            sum = Math.min(sum, matrix[row][col] + solve(matrix, row+1, col, dp));
        }

        if (prevCol >= 0) {
            dp[row][prevCol] = sum;
        }
        return sum;
    }
}
