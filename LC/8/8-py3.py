class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        is_decimal, is_negative, has_sign, has_value = False, False, False, False
        output = []
        for char in s:
            if char == ' ':
                if has_value or has_sign or is_decimal:
                    break
                continue
            
            if not char.isdigit() and\
                (char not in ('+','-','.') or has_value):
                    break
                
            if char == '+':
                if has_sign or is_negative:
                    break
                has_sign = True
            elif char == '-':
                if is_negative or has_sign:
                    break
                is_negative, has_sign = True, True
            elif char.isdigit():
                has_value = True
                output.append(char)
            elif char == '.':
                if is_decimal:
                    break
                is_decimal = True
                output.append(char)
            else:
                break
        
        if not output or not has_value:
            return 0
        
        num = floor(float("".join(output))) if is_decimal else int("".join(output))
        num = num if not is_negative else -num
        return max(pow(-2,31), min(pow(2,31)-1, num))
