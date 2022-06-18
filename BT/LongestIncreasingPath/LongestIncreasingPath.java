import java.util.*;

class Solution {
    static final int[][] DIRS = {{-1,0},{0,1},{1,0},{0,-1}};

    public int solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;

        int m = matrix.length,
            n = matrix[0].length;
        int maxPath = 0;
        int[][] memo = new int[m][n];
        boolean[][] visited = new boolean[m][n];

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (memo[row][col] > 0) continue;
                maxPath = Math.max(maxPath, traverse(matrix, row, col, visited, memo));
            }
        }
        return maxPath;
    }

    private int traverse(int[][] matrix, int row, int col, boolean[][] visited, int[][] memo) {
        int m = matrix.length,
            n = matrix[0].length;

        if (memo[row][col] > 0) return memo[row][col];
        if (visited[row][col]) return 0;
        visited[row][col] = true;

        int maxPath = 1;
        for (int[] dir: this.DIRS) {
            int r = dir[0] + row;
            int c = dir[1] + col;

            if (
                r < 0 || r >= m ||
                c < 0 || c >= n ||
                visited[r][c] ||
                matrix[row][col] <= matrix[r][c]
            ) continue;

            maxPath = Math.max(maxPath, 1 + traverse(matrix, r, c, visited, memo));
        }
        visited[row][col] = false;
        memo[row][col] = maxPath;
        return maxPath;
    }
}
