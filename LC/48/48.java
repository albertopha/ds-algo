/*
Input 1:
[1,2,3]
[4,5,6]
[7,8,9]


[0][0] => [0][n-1]
[0][1] => [1][n-1]
[0][2] => [n-1][n-1]

[1][0] => [0][1]
[1][1] => [1][1]
[1][n-1] => [n-1][1]

[n-1][0] => [0][0]
[n-1][1] => [1][0]
[n-1][2] => [2][0]

Input 2:
[5, 1, 9, 11]
[2, 4, 8, 10]
[13, 3, 6, 7]
[15,14,12,16]

First line => [col][n-1]

Second line =>
[1][0] => [0][1]
[1][1] => [1][2]

*/
class Solution {
    public void rotate(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return;
        int left = 0, right = matrix.length-1;
        while (left < right) {
            rotate(matrix, left, right);
            left++;
            right--;
        }
    }
    
    private void rotate(int[][] matrix, int left, int right) {
        if (left >= right) return;
        for (int shift = 0; shift < right-left; shift++) {
            // For readability
            int top = left,
                bottom = right;
            
            // Save the value of top left
            int topLeft = matrix[top][left+shift];
            
            // Rotate in reverse order
            matrix[top][left+shift] = matrix[bottom-shift][left];
            matrix[bottom-shift][left] = matrix[bottom][right-shift];
            matrix[bottom][right-shift] = matrix[top+shift][right];
            matrix[top+shift][right] = topLeft;
        }
    }
}
