import java.util.*;

/*
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]

[3, 6, 9],
[2, 5, 8],
[1, 4, 7]

0,0 -> 2,0 -> 2,2, 0,2

start = 0, end = len-1
    i = 0 -> end - start
        top left = [start][start+i]
        bottom left = [end-i][start]
        bottom right = [end][end-i]
        top right = [start+i][end]

0,1 -> 1,0 -> 2,1 -> 1,2



[1,  2, 3, 4]
[5,  6, 7, 8]
[9, 10,11,12]
[13,14,15,16]

0,1 -> 2,0 -> 3,2 -> 1,3

start = 0, end = len-1
    i = 1
        top left = [start][i] => [0][1]
        bottom left = [end-i][start] => [2][0]
        bottom right = [end][end-i] => [3][2]
        top right = [i][end] => [1][3]
*/

class Solution {
    public int[][] solve(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return matrix;

        int left = 0,
            right = matrix.length-1;
        
        while (left < right) {
            
            for (int i = 0; i < right - left; i++) {
                int top = left,
                    bottom = right;

                int topLeft = matrix[top][left+i];
                int bottomLeft = matrix[bottom-i][left];
                int bottomRight = matrix[bottom][right-i];
                int topRight = matrix[top+i][right];

                matrix[bottom-i][left] = topLeft;
                matrix[bottom][right-i] = bottomLeft;
                matrix[top+i][right] = bottomRight;
                matrix[top][left+i] = topRight;
            }
            left++;
            right--;
        }

        return matrix;
    }
}
