class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (s.length() == 0 || wordDict.size() == 0) return false;
        
        Map<Character, List<String>> firstCharMap = new HashMap<>();
        Boolean[] dp = new Boolean[s.length()];
        
        for (String word: wordDict) {
            char firstChar = word.charAt(0);
            if (!firstCharMap.containsKey(firstChar))
               firstCharMap.put(firstChar, new ArrayList<String>());
            firstCharMap.get(firstChar).add(word);
        }
        
        return wordBreakHelper(s, 0, firstCharMap, dp);
    }
    
    private boolean wordBreakHelper(String s, int i, Map<Character, List<String>> firstCharMap, Boolean[] dp) {
        if (i >= s.length()) return true;
        
        char firstChar = s.charAt(i);
        if (!firstCharMap.containsKey(firstChar)) {
            dp[i] = false;
            return false;
        }
        
        if (dp[i] != null) return dp[i];
        
        for (String word: firstCharMap.get(firstChar)) {
            if (s.startsWith(word, i) && wordBreakHelper(s, i+word.length(), firstCharMap, dp))
                return true;
        }
        
        dp[i] = false;
        return false;
    }
}
