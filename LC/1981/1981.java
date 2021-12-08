/*
[1,2,3],
[4,5,6],
[7,8,9]
*/
class Solution {
    public int minimizeTheDifference(int[][] mat, int target) {
        if (mat.length == 0 || mat[0].length == 0) return target;
        Integer[][] dp = new Integer[mat.length][4900];
        return minimize(mat, 0, 0, target, dp);
    }
    
    private int minimize(int[][] mat, int row, int sum, int target, Integer[][] dp) {
        if (row == mat.length) return Math.abs(target - sum);
        if (dp[row][sum] != null) return dp[row][sum];
        
        int minVal = Integer.MAX_VALUE;
        for (int col = 0; col < mat[0].length; col++) {
            int val = mat[row][col];
            minVal = Math.min(minVal, minimize(mat, row+1, sum+val, target, dp));
        }
        dp[row][sum] = minVal;
        return minVal;
    }
}
