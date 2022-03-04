import java.util.*;

class Solution {
    static final int POS_A_UPPER = (int) 'A';
    static final int POS_A_LOWER = (int) 'a';

    public boolean solve(String s) {
        int[] counter = getCounter(s);
        return validate(counter);
    }

    private boolean validate(int[] counter) {
        boolean oddFound = false;

        for (int i = 0; i < counter.length; i++) {
            if (counter[i] % 2 == 1) {
                if (oddFound) return false;
                oddFound = true;
            }
        }

        return true;
    }

    private int[] getCounter(String s) {
        int[] counter = new int[52];
        
        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            int chrInt = (int) chr;
            int position = (Character.isUpperCase(chr))
                ? (chrInt - this.POS_A_UPPER + 26)
                : chrInt - this.POS_A_LOWER;
            counter[position]++;
        }
        return counter;
    }
}
