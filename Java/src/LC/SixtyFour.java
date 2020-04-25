class Solution {
    public int minPathSum(int[][] grid) {
        if(grid.length == 0 && grid[0].length == 0) return 0;
        
        int columnLen = grid[0].length;
        int rowLen = grid.length;
        
        for(int i = 1; i < columnLen; i++) {
            grid[0][i] += grid[0][i-1];
        }
        
        for(int j = 1; j < rowLen; j++) {
            grid[j][0] += grid[j-1][0];
        }
        
        for(int i = 1; i < rowLen; i++) {
            for(int j = 1; j < columnLen; j++) {
                grid[i][j] += Math.min(grid[i-1][j], grid[i][j-1]);
            }
        }
        
        return grid[rowLen-1][columnLen-1];
    }
}