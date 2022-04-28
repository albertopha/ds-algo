"""
[23,2,4,6,7], k = 6
[23,25,29,35,42]
[5,1,5,5,0]
29, 35
5 , 5
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        total_sum = 0
        modulos = {0:-1}
        
        for i, num in enumerate(nums):
            total_sum += num
            modulo_sum = total_sum % k
            if modulo_sum in modulos:
                if i - modulos[modulo_sum] >= 2:
                    return True
            else:
                modulos[modulo_sum] = i
        return False
            
