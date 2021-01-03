/*
"aa"  "p"
 ^     ^

"aa"  "*"
  ^    ^

"cb"  "?a"
  ^     ^
  
   "" | a | a | a | a | a |
   -------------------------
""| T | F | F | F | F | F |
   ------------------------- 
* | T | T | T | T | T | T |
   -------------------------
a | F | T | T | T | T | T |
   -------------------------
  
   "" | a | d | c | e | b |
   -------------------------
""| T | F | F | F | F | F |
   ------------------------- 
* | T | T | T | T | T | T |
   -------------------------
a | F | T | F | F | F | F |
   -------------------------
* | F | T | T | T | T | T | 
   -------------------------
b | F | F | F | F | F | T |
   -------------------------
*/

class Solution {
    public boolean isMatch(String s, String p) {
        return isMatchDP(s, p);
        // retur isMatchBruteForce(s, p, 0, 0);
    }
    
    private boolean isMatchBruteForce(String s, String p, int si, int sp) {
        if (si >= s.length() || sp >= p.length()) {
            return si == s.length() && sp == p.length();
        }
        
        if (p.charAt(sp) != '*') {
            if (p.charAt(sp) != '?' && s.charAt(si) != p.charAt(sp)) {
                return false;
            }
            return isMatchBruteForce(s, p, si + 1, sp + 1);
        }
        
        boolean isMatching = isMatchBruteForce(s, p, si, sp + 1) ||
            isMatchBruteForce(s, p, si + 1, sp);
        
        return isMatching;
    }
    
    private boolean isMatchDP(String s, String p) {
        int colLen = s.length() + 1;
        int rowLen = p.length() + 1;
        
        boolean[][] dp = new boolean[rowLen][colLen];
        // empty string
        dp[0][0] = true; 
        
        // Fill first row
        for (int row = 1; row < rowLen; row++) {
            if (p.charAt(row-1) == '*') {
                dp[row][0] = dp[row-1][0];
            }
        }
        
        for (int row = 1; row < rowLen; row++) {
            for (int col = 1; col < colLen; col++) {
                if (p.charAt(row-1) == '*') {
                    dp[row][col] = dp[row-1][col] || dp[row][col-1];
                    continue;
                }
                
                if (p.charAt(row-1) == '?' || (s.charAt(col-1) == p.charAt(row-1))) {
                    dp[row][col] = dp[row-1][col-1];
                }
            }
        }
        
        // for (int i = 0; i < dp.length; i++) {
        //     System.out.println(Arrays.toString(dp[i]));
        // }
        
        return dp[rowLen-1][colLen-1];
    }
}
