class Solution {
    public boolean isValid(String s) {
        if (s.length() == 0) {
            return true;
        }
        
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        
        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            if (!map.containsKey(chr)) {
                stack.push(chr);
                continue;
            }
            
            if (stack.isEmpty() || stack.pop() != map.get(chr)) return false;
        }
        
        return stack.isEmpty();
    }
}
