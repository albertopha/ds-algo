class Solution {
    public int longestPalindromeSubseq(String s) {
        if (s.length() == 0) return 0;
        int[][] memo = new int[s.length()][s.length()];
        return longest(s, 0, s.length()-1, memo);
    }
    
    private int longest(String s, int start, int end, int[][] memo) {
        if (start > end) return 0;
        if (start == end) return 1;
        if (memo[start][end] != 0) return memo[start][end];
        memo[start][end] = (s.charAt(start) == s.charAt(end))
            ? 2 + longest(s, start+1, end-1, memo)
            : Math.max(longest(s, start+1, end, memo), longest(s, start, end-1, memo));
        return memo[start][end];
    }
}