import random
from collections import defaultdict

class Solution:

    """
    [Optimal for time]
    
    def __init__(self, nums: List[int]):
        self.lookup = defaultdict(list)
        for i, num in enumerate(nums):
            self.lookup[num].append(i)

    def pick(self, target: int) -> int:
        if target not in self.lookup:
            return -1
        
        indices = self.lookup[target]
        rand = random.randint(0, len(indices)-1)
        return indices[rand]
    """
    
    """
    [Optimal for space] TLE
    Reservoir Sampling
    https://www.youtube.com/watch?v=A1iwzSew5QY
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        if not self.nums:
            return -1
        
        duplicates = 0
        output = -1
        
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            
            if random.randint(0, duplicates) == 0:
                output = i
            duplicates += 1
        return output

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
