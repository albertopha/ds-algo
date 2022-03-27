/*
1432219, k = 1
[1,2,1,9]

14320, k = 0
[1,2,0]

123450, k = 5
[1,2,3,4,0]
*/
class Solution {
    public String removeKdigits(String num, int k) {
        if (num == null || num.length() == k) return "0";
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < num.length(); i++) {
            char chr = num.charAt(i);
            int value = Character.getNumericValue(chr);
            while (k > 0 && !stack.isEmpty() && Character.getNumericValue(stack.peek()) > value) {
                stack.pop();
                k--;
            }
            
            if (!stack.isEmpty() || value > 0) stack.add(chr);
        }
        
        while (k > 0 && !stack.isEmpty()) {
            stack.pop();
            k--;
        }
        
        String output = "";
        while (!stack.isEmpty()) {
            output = stack.pop() + output;
        }
        return (output.length() == 0) ? "0" : output;
    }
}
