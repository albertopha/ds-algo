class Solution {
    public int minFallingPathSum(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        for (int row = 1; row < m; row++) {
            for (int col = 0; col < n; col++) {
                int left = (col - 1) < 0 ? Integer.MAX_VALUE : matrix[row-1][col-1];
                int mid = matrix[row-1][col];
                int right = (col + 1) >= m ? Integer.MAX_VALUE : matrix[row-1][col+1];
                matrix[row][col] += Math.min(left, Math.min(mid, right));
            }
        }
        int minSum = Integer.MAX_VALUE;
        for (int col = 0; col < n; col++) minSum = Math.min(minSum, matrix[m-1][col]);
        return minSum;
    }
}
