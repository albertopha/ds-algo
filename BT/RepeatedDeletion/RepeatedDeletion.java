import java.util.*;

class Solution {
    public String solve(String s) {
        if (s.length() <= 1) return s;

        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (stack.isEmpty() || stack.peek() != s.charAt(i)) {
                stack.push(s.charAt(i));
                continue;
            }
            
            if (stack.peek() == s.charAt(i)) {
                while (i < s.length() && s.charAt(i) == stack.peek()) i++;
                stack.pop();
                i--;
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        return sb.reverse().toString();
    }
}
