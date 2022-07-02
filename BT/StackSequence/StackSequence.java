import java.util.*;

class Solution {
    public boolean solve(int[] pushes, int[] pops) {
        if (pushes.length != pops.length) return false;
        Stack<Integer> stack = new Stack<>();

        int popsIndex = 0;
        for (int i = 0; i < pushes.length; i++) {

            stack.push(pushes[i]);
            while (
                !stack.isEmpty() &&
                popsIndex < pops.length &&
                stack.peek() == pops[popsIndex]
            ) {
                stack.pop();
                popsIndex++;
            }
        }
        return stack.isEmpty();
    }
}
