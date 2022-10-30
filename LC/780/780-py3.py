"""
x, y
    (x+y, y), (x, x+y)
    /       \
"""

from collections import deque

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if (sx, sy) == (tx, ty):
            return True
        
        if tx < sx or ty < sy:
            return False
        
        if tx == sx:
            return (ty - sy) % sx == 0
        
        if ty == sy:
            return (tx - sx) % sy == 0 
        
        return self.reachingPoints(sx, sy, tx % ty, ty) if tx > ty else self.reachingPoints(sx, sy, tx, ty % tx)
    
    def reachingPointsBruteForce(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if (sx, sy) == (tx, ty):
            return True
        
        queue = deque([(sx, sy)])
        visited = set()
        
        while queue:
            position = queue.popleft()
            if position == (tx, ty):
                return True
            
            visited.add(position)
            x, y = position
            for dirx, diry in [[y,0],[0,x]]:
                newx, newy = x+dirx, y+diry
                if (newx, newy) in visited or\
                    newx > tx or newy > ty:
                    continue
                queue.append((newx, newy))
            
        return False
