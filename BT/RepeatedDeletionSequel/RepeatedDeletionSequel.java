import java.util.*;

class Solution {
    public String solve(String s, int k) {
       if (s.length() == 0 || k == 0) return s;
       
       Stack<int[]> stack = new Stack<>();
       for (int i = 0; i < s.length(); i++) {
           if (stack.isEmpty() || getChar(s, stack.peek()[0]) != s.charAt(i)) {
               stack.push(new int[]{i, 0});
           }
           
           stack.peek()[1]++;
           if (stack.peek()[1] == k) stack.pop();
       }

       StringBuilder sb = new StringBuilder();
       while (!stack.isEmpty()) {
           int[] curr = stack.pop();
           while (curr[1]-- > 0) {
            sb.append(getChar(s, curr[0]));
           }
       }
       return sb.reverse().toString();
    }

    private Character getChar(String s, int index) {
        return s.charAt(index);
    }
}
