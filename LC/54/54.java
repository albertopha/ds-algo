class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> output = new ArrayList<>();
        if (matrix.length == 0 || matrix[0].length == 0) {
            return output;
        }
        
        int m = matrix.length,
            n = matrix[0].length;
        
        int left = 0, right = n-1;
        int top = 0, bottom = m-1;
        int count = m * n;
        
        while (count > 0) {
            // Left to right
            for (int col = left; col <= right; col++) {
                output.add(matrix[top][col]);
                count--;
            }
            top++;
            
            if (count == 0) break;
            
            // Top to bottom
            for (int row = top; row <= bottom; row++) {
                output.add(matrix[row][right]);
                count--;
            }
            right--;
            
            if (count == 0) break;
            
            // Right to left
            for (int col = right; col >= left; col--) {
                output.add(matrix[bottom][col]);
                count--;
            }
            bottom--;
            if (count == 0) break;
            
            // Bottom to top
            for (int row = bottom; row >= top; row--) {
                output.add(matrix[row][left]);
                count--;
            }
            left++;
        }
        return output;
    }
}
