/*
0, 1, 6&9, 8,

"101", "111", "181", "609", "619", "689", "808", "818", "888", "906", "916", "986"
*/
import java.util.*;

class Solution {
    private final Map<Character, Character> matches = new HashMap<>();
    public Solution() {
        this.matches.put('0','0');
        this.matches.put('1','1');
        this.matches.put('6','9');
        this.matches.put('8','8');
        this.matches.put('9','6');
    }

    public String[] solve(int n) {
        if (n <= 0) return new String[0];
        List<String> output = new ArrayList<>();
        getUpsideDowns(n, n, new StringBuilder(), output);
        String[] arrOutput = new String[output.size()];
        return output.toArray(arrOutput);
    }

    private void getUpsideDowns(int n, int count, StringBuilder value, List<String> output) {
        if (count == 0) {
            if (isValid(value)) {
                output.add(value.toString());
            }
            return;
        }

        for (char key: this.matches.keySet()) {
            // Preventing leading zeros
            if (n > 1 && value.length() == 0 && key == '0') continue;
            value.append(key);
            getUpsideDowns(n, count-1, value, output);
            value.deleteCharAt(value.length()-1);
        }
    }

    private boolean isValid(StringBuilder value) {
        int left = 0,
            right = value.length()-1;

        // Handing leading zero
        if (value.length() > 1 && value.charAt(0) == '0') return false;
        
        while (left <= right) {
            char leftChar = value.charAt(left);
            char rightChar = value.charAt(right);
            if (
                // Special handling for size == 1
                (left == right && leftChar != rightChar) ||
                this.matches.get(leftChar) != rightChar
            ) return false;
            left++;
            right--;
        }
        return true;
    }
}
