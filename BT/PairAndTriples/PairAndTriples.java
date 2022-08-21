import java.util.*;

class Solution {
    public boolean solve(String s) {
        if (s.length() < 2) return false;
        int[] counter = new int[10];
        for (int i = 0; i < s.length(); i++) {
            counter[Character.getNumericValue(s.charAt(i))]++;
        }
        boolean foundPair = false;
        for (int i = 0 ; i < counter.length; i++) {
            if (counter[i] == 1) return false;
            if (counter[i] == 2) {
                if (foundPair) return false;
                foundPair = true;
                counter[i] = 0;
            }
        }
        for (int i = 0; i < counter.length; i++) {
            if (counter[i] % 3 != 0) {
                if (foundPair) return false;
                counter[i] -= 2;
                if (counter[i] % 3 != 0) return false;
                foundPair = true; 
            }
        }
        return foundPair;
    }
}
