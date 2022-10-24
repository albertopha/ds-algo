"""
1. end must be in a bank
2. BFS like searching
"""
from collections import deque 

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or not bank or end not in bank:
            return -1
        
        if start == end:
            return 0
        
        queue = deque([(start, 0)])
        unvisited = set(bank)
        
        while queue:
            mutation, steps = queue.popleft()
                        
            if mutation == end:
                return steps
            
            updated_unvisited = set()
            for bank_mutation in unvisited:
                if bank_mutation == start:
                    continue
                    
                if self.isOneMutation(mutation, bank_mutation):
                    queue.append((bank_mutation, steps+1))
                else:
                    updated_unvisited.add(bank_mutation)
            unvisited = updated_unvisited
        return -1
    
    def isOneMutation(self, source, target) -> bool:
        diff = 0
        for i in range(len(source)):
            diff += 1 if source[i] != target[i] else 0
            if diff > 1:
                return False
        return diff == 1
        
