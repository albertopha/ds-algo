"""
-----------------------------------
stack = [1,2,1,9]
stack = [2,0,0]

12345, k = 3

stack = [1,2,3,4,5], k = 3

1000000, k = 1
stack = [0]

1234567890, k = 9
stack = [1,2,3,4,5,6,7,8,0], k = 8

-----------------------------------
Test cases:
"1432219"
3
"100000"
2
"12345"
3
"10200"
1
"10"
2
"112"
1
"1234567890"
9
-----------------------------------
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or k == 0:
            return num
        
        stack = [num[0]]
        
        for i in range(1, len(num)):
            val = int(num[i])
            while k > 0 and stack and int(stack[-1]) > val:
                stack.pop()
                k-=1
            
            if stack or val > 0:
                stack.append(num[i])
        
        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        return "".join(stack) if stack else "0"
