import java.util.*;

class Solution {
    public int solve(String s) {
        if (s.length() == 0) return 0;

        Stack<Character> stack = new Stack<>();
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);

            if (stack.isEmpty()) {
                if (chr == ')') count++;
                else stack.push(chr);
                continue;
            }

            if (chr == ')') stack.pop();
            else stack.push(chr);
        }

        return count + stack.size();
    }
}
