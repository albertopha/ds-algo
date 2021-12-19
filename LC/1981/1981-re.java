/* P2, Dec.19, 2021 */
class Solution {
    public int minimizeTheDifference(int[][] mat, int target) {
        if (mat.length == 0 || mat[0].length == 0) return 0;
        Integer[][] memo = new Integer[mat.length][5000];
        return getMinDiffs(mat, 0, 0, target, memo);
    }
    
    private int getMinDiffs(int[][] mat, int row, int sum, int target, Integer[][] memo) {
        if (row == mat.length) {
            return Math.abs(target - sum);
        }
        
        if (memo[row][sum] != null) return memo[row][sum];
        
        int minDiff = Integer.MAX_VALUE;
        for (int col = 0; col < mat[0].length; col++) {
            minDiff = Math.min(
                minDiff,
                getMinDiffs(mat, row+1, sum+mat[row][col], target, memo)
            );
        }
        
        memo[row][sum] = minDiff;
        return minDiff;
    }
}
