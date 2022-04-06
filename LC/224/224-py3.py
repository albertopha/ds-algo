"""
1 + 1

[1,+,1]
num1 = 1
op = +
num2 = 1

2-1 + 2
-1+2
[2,+,1,-]

[2,-,1,+,2]

(1+(4+5+2)-3)+(6+8)
[14,),3,-,),]

(-3+4)

[),4,+,3,-]

"""
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        i = len(s)-1
        while i >= 0:
            # White space
            if s[i] == ' ':
                i -= 1
                continue
            
            # Open bracket
            if s[i] == '(':
                val = 0
                op = ''
                if stack[-1] == '-':
                    stack.pop()
                    val = -stack.pop()
                else:
                    val = stack.pop()
                    
                while stack[-1] != ')':
                    op = stack.pop()
                    next_val = stack.pop()
                    val = self.compute(val, next_val, op)
                stack.pop()
                stack.append(val)
                i -= 1
                continue
            
            # Operator
            if s[i] == '+' or s[i] == '-' or s[i] == ')':
                stack.append(s[i])
                i -= 1
                continue
            
            # Numeric
            val = ''
            while i >= 0 and s[i].isnumeric():
                val = s[i] + val
                i -= 1
            stack.append(int(val))
        
        val = 0
        op = ''
        if stack[-1] == '-':
            stack.pop()
            val = -stack.pop()
        else:
            val = stack.pop()
        
        while stack:
            op = stack.pop()
            next_val = stack.pop()
            val = self.compute(val, next_val, op)
        
        return val
                
    def compute(self, val1: int, val2: int, op: str) -> int:
        if op == '+':
            return val1 + val2
        if op == '-':
            return val1 - val2
        return 0
