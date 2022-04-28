from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0        
        
        i = 0
        dq = deque()
        
        while i < len(s):
            if s[i] == ' ':
                i+=1
                continue
                
            if s[i] in ('+','-','*','/'):
                dq.append(s[i])
                i+=1
                continue
            
            e = i
            while i < len(s) and s[i].isnumeric():
                i+=1
            
            num = int(s[e:i])
            if dq and dq[-1] in ('*','/'):
                op = dq.pop()
                prev_num = dq.pop()
                dq.append(self.evaluate(prev_num, num, op))
            else:
                dq.append(num)
        
        num = dq.popleft()
        while dq:
            op = dq.popleft()
            prev_num = dq.popleft()
            num = self.evaluate(num, prev_num, op)
        return num
    
    def evaluate(self, num1: int, num2: int, op: str) -> int:
        if op == '+':
            return num1 + num2
        if op == '-':
            return num1 - num2
        if op == '/':
            return num1 // num2
        if op == '*':
            return num1 * num2
        return 0
