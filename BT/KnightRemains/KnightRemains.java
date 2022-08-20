import java.util.*;

class Solution {
    static final int[][] DIRS = {{2,-1},{2,1},{-2,-1},{-2,1},{1,-2},{-1,-2},{1,2},{-1,2}};
    public int solve(int n, int x, int y, int k) {
        if (n == 0) return 0;
        Double[][][] memo = new Double[n][n][k+1];
        double rate = dfs(n, x, y, k, memo);
        return (int) Math.floor(rate * 100);
    }

    private double dfs(int n, int x, int y, int k, Double[][][] memo) {
        if (x < 0 || x >= n || y < 0 || y >= n) return 0;
        if (k == 0) return 1;
        if (memo[x][y][k] != null) return memo[x][y][k];
        double rate = 0;
        for (int[] dirs: DIRS) {
            int nX = x + dirs[0];
            int nY = y + dirs[1];
            rate += 0.125 * dfs(n, nX, nY, k-1, memo);
        }
        memo[x][y][k] = rate;
        return rate;
    }
}
