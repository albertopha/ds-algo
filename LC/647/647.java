class Solution {
    public int countSubstrings(String s) {
        int len = s.length();
        if (len == 0) return 0;
        
        int count = len;
        boolean[][] dp = new boolean[len][len];
        
        // Diagonal (single character)
        for (int i = 0; i < len; i++) dp[i][i] = true;
        
        // Two characters
        for (int i = 0; i < len-1; i++) {
            if (s.charAt(i) == s.charAt(i+1)) {
                dp[i][i+1] = true;
                count++;
            };
        }
        
        for (int i = 2; i < len; i++) {
            int row = 0;
            int col = i;
            
            while (col < len) {
                if (s.charAt(row) == s.charAt(col) && dp[row+1][col-1]) {
                    dp[row][col] = true;
                    count++;
                }
                row++;
                col++;
            }
        }
        
        return count;
    }
}
