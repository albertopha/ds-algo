/**
A -> "1"
B -> "2"
...
Z -> "26"

                        11106
                        /   \
                 A + 1106   11 + 106
                 /       \
        A + A + 106  A + 11 + 06
*/
class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0 || s.charAt(0) == '0') return 0;
        int[] dp = new int[s.length()];
        Arrays.fill(dp, -1);
        return numDecodings(s, 0, dp);
    }
    
    private int numDecodings(String s, int index, int[] dp) {
        if (index >= s.length()) return 1;
        if (dp[index] != -1) return dp[index];
        if (s.charAt(index) == '0') return 0;
        
        int singleDigit = numDecodings(s, index+1, dp);
        int doubleDigit = 0;
        
        if (index + 1 < s.length() &&
            Integer.parseInt(s.substring(index, index+2)) <= 26
        ) {
            doubleDigit = numDecodings(s, index+2, dp);
        }
        
        dp[index] = singleDigit + doubleDigit;
        return dp[index];
    }
}