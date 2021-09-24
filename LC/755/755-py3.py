class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        if not heights or not volume:
            return []
        
        for _ in range(volume):
            idx = k
            
            # Moving from k to left
            while idx > 0 and heights[idx-1] <= heights[idx]:
                idx -= 1
            
            # Moving from left to right
            while idx < len(heights)-1 and heights[idx] >= heights[idx+1]:
                idx += 1
            
            # Moving from right to K
            while idx > k and heights[idx-1] <= heights[idx]:
                idx -= 1
            
            heights[idx] += 1
        
        return heights