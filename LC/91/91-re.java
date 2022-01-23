/*
226
=>                  226
                /           \
            2, 26           22, 6
            /   |           |    \
       2,2,6   2,26       22,6
*/
class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0) return 0;
        return numDecodings(s, 0, new HashMap<Integer, Integer>());
    }
    
    private int numDecodings(String s, int i, Map<Integer, Integer> dp) {
        if (i >= s.length()) return 1;
        if (s.charAt(i) == '0') return 0;
        if (dp.containsKey(i)) return dp.get(i);
        
        int first = numDecodings(s, i+1, dp);
        int second = 0;
        
        if (i+2 <= s.length() && Integer.parseInt(s.substring(i, i+2)) <= 26) {
            second = numDecodings(s, i+2, dp);
        }
        
        dp.put(i, first+second);
        return first+second;
    }
}
