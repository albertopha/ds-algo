from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        
        for value in counter.values():
            if value > 1:
                return True
            
        return False
