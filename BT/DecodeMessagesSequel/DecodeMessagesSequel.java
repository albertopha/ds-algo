import java.util.*;

/*
22 -> 2 + 22

51*6*
 ^

    5
    |           \ ... \
    1           11 ... 19
  / | \ ... \
 1  2  3 ... 9

Note: working except extremly long strings due to not
handling modulo properly.
ie. "1**12345******123412341234123412412341234"
*/

class Solution {
    static final int MODULO = 1000000007;

    public int solve(String message) {
        if (message.length() == 0) return 0;
        long[] memo = new long[message.length()];
        Arrays.fill(memo, -1);
        return solve(message, 0, memo);
    }

    private int solve(String message, int index, long[] memo) {
        if (index >= message.length()) return 1;
        if (memo[index] >= 0) return (int) memo[index];
        if (message.charAt(index) == '0') return 0;

        int singleDigit = (message.charAt(index) == '*')
            ? 9 * solve(message, index+1, memo)
            : solve(message, index+1, memo);
        int doubleDigit = isEligibleForDoubleDigit(message, index)
            ? getDoubleDigitMultiplier(message, index) * solve(message, index+2, memo)
            : 0;

        memo[index] = (singleDigit + doubleDigit) % MODULO;
        return (int) memo[index];
    }

    private boolean isEligibleForDoubleDigit(String message, int index) {
        if (index + 1 >= message.length()) return false;

        String substr = message.substring(index, index+2);
        char firstChar = substr.charAt(0);
        char secondChar = substr.charAt(1);

        return (
            firstChar == '*' ||
            secondChar == '*' ||
            (
                Integer.parseInt(substr) >= 10 &&
                Integer.parseInt(substr) <= 26
            )
        );
    }

    private int getDoubleDigitMultiplier(String message, int index) {
        char firstChar = message.charAt(index);
        char secondChar = message.charAt(index+1);

        // 10 - 19 && 20 - 26 => 15 variations
        if (firstChar == '*' && secondChar == '*') {
            return 15;
        }
    
        if (firstChar == '*') {
            int secondVal = Character.getNumericValue(secondChar);
            return (secondVal <= 6) ? 2 : 1;
        }

        if (secondChar == '*') {
            int firstVal = Character.getNumericValue(firstChar);
            return (firstVal == 1) ? 9 : (firstVal == 2) ? 6 : 0;
        }
        return 1;
    }
}
