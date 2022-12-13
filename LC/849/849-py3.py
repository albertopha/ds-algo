"""
[1,0,1] => (2-0) // 2 = 1
[1,0,0,1] => (3-0) // 2 = 1
[1,0,0,0,1] => (4-0) // 2 = 2 
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if not seats:
            return 0
        
        prev_occupied = seats.index(1)
        max_distance = prev_occupied
        for i in range(prev_occupied+1, len(seats)):
            if seats[i] == 1:
                max_distance = max((i-prev_occupied) // 2, max_distance)
                prev_occupied = i
        
        return max(len(seats)-1-prev_occupied, max_distance)
