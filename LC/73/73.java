/*

Example 1)
[1,1,1]
[1,0,1]
[1,1,1]

rows = [1,0,1]
cols = [1,0,1]


*/
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        if (m == 0 || n == 0) return;
        boolean[] rows = new boolean[m];
        boolean[] cols = new boolean[n];
        
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (matrix[row][col] == 0) {
                    rows[row] = true;
                    cols[col] = true;
                }
            }
        }
        
        
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (rows[row] || cols[col]) matrix[row][col] = 0;
            }
        }
    }
}
