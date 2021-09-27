/**
s = aa
     ^
p = a
     ^
     
s = aa
     ^
p = a*a
      ^
      
s = abcdef
    ^
p = .*
     ^
   | ""| a | a | b
--------------------------------
"" | T | F | F | F
c  | F | F | F | F
*  | T | F | F | F
a  | F | T | F | F
*  | T | T | T | F
b  | F | F | F | T
*/
class Solution {
    public boolean isMatch(String s, String p) {
        if (s.length() == 0 || p.length() == 0) {
            return s.length() == p.length();
        }
        
        boolean[][] dp = new boolean[p.length()+1][s.length()+1];
        dp[0][0] = true; // starting point (empty strings)
        
        // Fill the first row
        for (int row = 1; row < dp.length; row++) {
            char pChar = p.charAt(row-1);
            if (pChar == '*') {
                dp[row][0] = dp[row-2][0];
            }
        }
        
        // Fill the rest
        for (int row = 1; row < dp.length; row++) {
            char pChar = p.charAt(row-1);
            for (int col = 1; col < dp[0].length; col++) {
                char sChar = s.charAt(col-1);
                
                if (sChar == pChar || pChar == '.') {
                    dp[row][col] = dp[row-1][col-1];
                } else if (pChar == '*') {
                    char prevChar = p.charAt(row-2);
                    if (prevChar == '.' || prevChar == sChar) {
                        dp[row][col] = dp[row-2][col] || dp[row-1][col] || dp[row][col-1];
                    } else {
                        dp[row][col] = dp[row-2][col];
                    }
                }
            }
        }
        return dp[dp.length-1][dp[0].length-1];
    }
}