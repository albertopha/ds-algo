class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        ast_stack = []
        
        for i in range(len(s)):
          ch = s[i]
          if ch == "(":
            stack.append(i)
          elif ch == "*":
            ast_stack.append(i)
          else:
            if len(stack) > 0:
              stack.pop()
            elif len(ast_stack) > 0:
              ast_stack.pop()
              continue
            else:
              return False
        
        if (len(stack) == 0):
          return True
        
        if (len(ast_stack) == 0):
          return False
        # print(stack)
        # print(ast_stack)
        stack.reverse()
        for l in stack:
          flag = False
          for i in range(len(ast_stack)-1, -1, -1):
            ast = ast_stack[i]
            # print('l = ', l, ' ast = ', ast)
            if ast == -1:
              continue

            if l <= ast:
              flag = True
              ast_stack[i] = -1
              break
            else:
              flag = False
          if not flag:
            # print('NOT l = ', l, ' ast = ', ast)
            return False
        return True
            