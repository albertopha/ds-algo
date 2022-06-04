"""
123
[123]

12345
[12,345]

0 -> [Zero]
1 - 9 -> [One, ..., Nine]
10 - 19 -> [Ten, Nineteen]
20/30/40/50/60/70/80/90 ->


"""
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        suffix = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
        nums = self.numbersToArr(num)
        for i, num in enumerate(nums):
            words = self.getNumberWords(num)
            nums[i] = (words + ' ' + suffix[i]).strip() if words else ''
        nums.reverse()
        return (' '.join(list(filter(lambda word: word, nums)))).strip()
        
    def getNumberWords(self, num: int) -> str:
        if num <= 9:
            return self.getSingleDigitWord(num)
        
        if num <= 19:
            return self.getTwoDigitsTenthsWord(num)
        
        if num < 100:
            return (self.getTwoDigitTensWord(num // 10 * 10) + ' ' + self.getNumberWords(num % 10)).strip()
        
        return (self.getNumberWords(num // 100) + ' Hundred' + ' ' + self.getNumberWords(num % 100)).strip()
        
    
    def getTwoDigitTensWord(self, num: int) -> str:
        if num == 20:
            return 'Twenty'
        if num == 30:
            return 'Thirty'
        if num == 40:
            return 'Forty'
        if num == 50:
            return 'Fifty'
        if num == 60:
            return 'Sixty'
        if num == 70:
            return 'Seventy'
        if num == 80:
            return 'Eighty'
        if num == 90:
            return 'Ninety'
        return ''
    
    def getTwoDigitsTenthsWord(self, num: int) -> str:
        if num == 10:
            return 'Ten'
        if num == 11:
            return 'Eleven'
        if num == 12:
            return 'Twelve'
        if num == 13:
            return 'Thirteen'
        if num == 14:
            return 'Fourteen'
        if num == 15:
            return 'Fifteen'
        if num == 16:
            return 'Sixteen'
        if num == 17:
            return 'Seventeen'
        if num == 18:
            return 'Eighteen'
        if num == 19:
            return 'Nineteen'
        return ''
        
    def getSingleDigitWord(self, num: int) -> str:
        if num == 1:
            return 'One'
        if num == 2:
            return 'Two'
        if num == 3:
            return 'Three'
        if num == 4:
            return 'Four'
        if num == 5:
            return 'Five'
        if num == 6:
            return 'Six'
        if num == 7:
            return 'Seven'
        if num == 8:
            return 'Eight'
        if num == 9:
            return 'Nine'
        return ''
        
    def numbersToArr(self, num: int) -> List[int]:
        nums = []
        
        while num > 0:
            nums.append(num % 1000)
            num //= 1000
        
        return nums
