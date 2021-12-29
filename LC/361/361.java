/*
============================================
Test cases:
[["0","E","0","0"],
 ["E","0","W","E"],
 ["0","E","0","0"]]
 
 
============================================
Brute force:
1. Traverse matrix:   --- O(R*C)
    a. On each cell with "0",  --- O(R+C)
        count # of "E" in the same row and col
    b. Update maxEnemy.

Time: O(R*C*(R+C))
Space: O(1)
============================================
Optimal (Time):
[["0","E","0","0"],
 ["E","0","W","E"],
 ["0","E","0","0"]]
 
 Row counts:
 [[1,2,0,0],
 [1,2,0,1],
 [1,2,0,1]]
 
 Col counts:
 [[1,1,1,1],
 [1,1,1,1],
 [1,1,1,1]]

============================================
*/
class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if(grid == null || grid.length == 0 || grid[0].length== 0) {
            return 0;
        }
        
        return bruteForce(grid);
    }
    
    private int bruteForce(char[][] grid) {
        int maxEnemies = 0;
        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                if (grid[row][col] == '0') {
                    maxEnemies = Math.max(maxEnemies, countEnemies(grid, row, col));
                }
            }
        }
        return maxEnemies;
    }
    
    private int countEnemies(char[][] grid, int row, int col) {
        int count = 0;
        for (int i = row; i < grid.length; i++) {
            if (grid[i][col] == 'W') {
                break;
            }
            if (grid[i][col] == 'E') {
                count++;
            }
        }
        
        for (int i = row; i >= 0; i--) {
            if (grid[i][col] == 'W') {
                break;
            }
            if (grid[i][col] == 'E') {
                count++;
            }
        }
        
        for (int i = col; i < grid[0].length; i++) {
            if (grid[row][i] == 'W') {
                break;
            }
            if (grid[row][i] == 'E') {
                count++;
            }
        }
        
        for (int i = col; i >= 0; i--) {
            if (grid[row][i] == 'W') {
                break;
            }
            if (grid[row][i] == 'E') {
                count++;
            }
        }
        
        return count;
    }
} 
