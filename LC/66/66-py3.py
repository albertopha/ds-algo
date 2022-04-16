class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        
        i = len(digits)-1
        rd = 1
        while i >= 0 and rd > 0:
            digits[i] += rd
            rd = digits[i] // 10
            digits[i] %= 10
            i -= 1
        if rd > 0:
            digits.insert(0, 1)
        return digits
