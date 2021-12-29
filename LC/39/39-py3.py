class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        output = []
        self.backtrack(candidates, target, 0, [], output)
        return output
        
    def backtrack(self, candidates: List[List[int]], target: int, index: int, current: List[int], output: List[List[int]]) -> None:
        if target == 0:
            output.append(current[:])
            return
        
        for i in range(index, len(candidates)):
            current.append(candidates[i])
            if target >= candidates[i]:
                self.backtrack(candidates, target-candidates[i], i, current, output)
            current.pop()
        
        
