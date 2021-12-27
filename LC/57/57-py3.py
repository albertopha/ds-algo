class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        insert_index = len(intervals)
        for i in range(len(intervals)):
            start = intervals[i][0]
            if newInterval[0] <= start:
                insert_index = i
                break
        
        intervals.insert(insert_index, newInterval)
        return self.merge(intervals)
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_end = merged_intervals[-1][1]
            new_start, new_end = intervals[i]
            
            if prev_end >= new_start:
                merged_intervals[-1][1] = max(prev_end, new_end)
            else:
                merged_intervals.append(intervals[i])
        return merged_intervals
