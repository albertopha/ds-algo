class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        maxLeft = self.getMax(height, 0, len(height), 1)
        maxRight = self.getMax(height, len(height)-1, -1, -1)
        trapped_area = 0
        
        for i, h in enumerate(height):
            trapped_area += (min(maxLeft[i], maxRight[i]) - h)
        return trapped_area
    
    def getMax(self, height: List[int], start: int, end: int, increment: int) -> List[int]:
        maxSeen = [0] * len(height)
        for i in range(start, end, increment):
            if i == 0 or i == len(height)-1:
                maxSeen[i] = height[i]
            else:
                prevSeen = maxSeen[i-1] if increment > 0 else maxSeen[i+1]
                maxSeen[i] = max(prevSeen, height[i])
        return maxSeen
        
