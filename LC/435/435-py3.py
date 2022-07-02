"""
[[1,2],[2,3],[3,4],[1,3]]

[1,2],[2,3],[1,3],[3,4]


"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or not intervals[0]:
            return 0
        
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        overlap = 0
        latest_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < latest_end:
                overlap+=1
            else:
                latest_end = end
            
        return overlap
