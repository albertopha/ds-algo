/*
ADOBECODEBANC, ABC
          ^
             ^

{
    A: 1
    B: 1,
    C: 1
}

unique: 2


ABC
^

{
    A: 1,
    B: 1,
    C: 1
}

*/
class Solution {
    public String minWindow(String s, String t) {
        if (s.length() == 0 || t.length() == 0) return "";
        if (s.length() < t.length()) return "";
        
        int l = 0;
        int count = 0;
        int minLeft = -1,
            maxRight = s.length();
        Map<Character, Integer> sCounter = new HashMap<>();
        Map<Character, Integer> tCounter = getCounter(t);
        
        for (int r = 0; r < s.length(); r++) {
            char chr = s.charAt(r);
            
            if (tCounter.containsKey(chr)) {
                int newCounter = sCounter.getOrDefault(chr, 0) + 1;
                sCounter.put(chr, newCounter);
                if (newCounter == tCounter.get(chr)) count++;
            }
            
            while (l <= r && count == tCounter.size()) {
                int prevSize = maxRight - minLeft + 1;
                int currSize = r - l + 1;
                if (prevSize > currSize) {
                    minLeft = l;
                    maxRight = r;
                }
                
                char leftChar = s.charAt(l);
                if (sCounter.containsKey(leftChar)) {
                    sCounter.put(leftChar, sCounter.get(leftChar)-1);
                    if (sCounter.get(leftChar) < tCounter.get(leftChar)) count--;
                    if (sCounter.get(leftChar) == 0) sCounter.remove(leftChar);
                }
                l++;
            }
        }
        return (minLeft == -1) ? "" : s.substring(minLeft, maxRight+1);
    }
    
    private Map<Character, Integer> getCounter(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            counter.put(chr, counter.getOrDefault(chr, 0) + 1);
        }
        return counter;
    }
}
