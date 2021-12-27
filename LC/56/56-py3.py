class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        
        # Sort by the end time
        intervals.sort(key=lambda i: i[1])
        # Sort by the start time
        intervals.sort(key=lambda i: i[0])
        
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_end = merged_intervals[-1][1]
            curr_start = intervals[i][0]
            
            if curr_start <= prev_end:
                merged_intervals[-1][1] = max(prev_end, intervals[i][1])
            else:
                merged_intervals.append(intervals[i])
        return merged_intervals
        
